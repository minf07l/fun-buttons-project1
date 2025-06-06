from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field
import uuid
from datetime import datetime
from typing import Optional


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")


# Define Models
class NumberData(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    number: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class SaveNumberRequest(BaseModel):
    number: float

class NumberResponse(BaseModel):
    number: Optional[float] = None
    exists: bool


# Add your routes to the router instead of directly to app
@api_router.get("/")
async def root():
    return {"message": "Number Storage API"}

@api_router.post("/save-number")
async def save_number(request: SaveNumberRequest):
    try:
        # Create number data object
        number_data = NumberData(number=request.number)
        
        # Clear existing numbers (keep only the latest)
        await db.numbers.delete_many({})
        
        # Insert new number
        await db.numbers.insert_one(number_data.dict())
        
        return {"success": True, "message": "Number saved successfully", "number": request.number}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving number: {str(e)}")

@api_router.get("/get-number", response_model=NumberResponse)
async def get_number():
    try:
        # Get the latest saved number
        latest_number = await db.numbers.find_one(sort=[("timestamp", -1)])
        
        if latest_number:
            return NumberResponse(number=latest_number["number"], exists=True)
        else:
            return NumberResponse(number=None, exists=False)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving number: {str(e)}")

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
