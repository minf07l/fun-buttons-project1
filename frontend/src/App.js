import React, { useState } from "react";
import "./App.css";
import { BrowserRouter, Routes, Route, Link, useNavigate } from "react-router-dom";
import axios from "axios";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

// Page 1: Save Number
const SavePage = () => {
  const [number, setNumber] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleSave = async () => {
    if (!number.trim()) {
      setMessage("Please enter a number");
      return;
    }

    setLoading(true);
    setMessage("");

    try {
      const response = await axios.post(`${API}/save-number`, {
        number: parseFloat(number)
      });
      
      setMessage(`Number ${number} saved successfully!`);
      setNumber("");
    } catch (error) {
      console.error("Error saving number:", error);
      setMessage("Error saving number. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <div className="container">
        <h1>Save Number</h1>
        <div className="form-group">
          <input
            type="number"
            value={number}
            onChange={(e) => setNumber(e.target.value)}
            placeholder="Enter a number"
            className="number-input"
          />
          <button 
            onClick={handleSave} 
            disabled={loading}
            className="save-btn"
          >
            {loading ? "Saving..." : "Save"}
          </button>
        </div>
        {message && <p className="message">{message}</p>}
        
        <div className="navigation">
          <Link to="/show" className="nav-link">Go to Show Page →</Link>
        </div>
      </div>
    </div>
  );
};

// Page 2: Show Number
const ShowPage = () => {
  const [savedNumber, setSavedNumber] = useState(null);
  const [loading, setLoading] = useState(false);
  const [hasNumber, setHasNumber] = useState(false);

  const handleShow = async () => {
    setLoading(true);
    
    try {
      const response = await axios.get(`${API}/get-number`);
      const data = response.data;
      
      if (data.exists) {
        setSavedNumber(data.number);
        setHasNumber(true);
      } else {
        setSavedNumber(null);
        setHasNumber(false);
      }
    } catch (error) {
      console.error("Error fetching number:", error);
      setSavedNumber(null);
      setHasNumber(false);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <div className="container">
        <h1>Show Number</h1>
        <button 
          onClick={handleShow} 
          disabled={loading}
          className="show-btn"
        >
          {loading ? "Loading..." : "Show"}
        </button>
        
        <div className="result">
          {savedNumber !== null ? (
            <p className="number-display">
              Last saved number: <span className="number">{savedNumber}</span>
            </p>
          ) : hasNumber === false && savedNumber === null && !loading ? (
            <p className="no-number">none</p>
          ) : null}
        </div>
        
        <div className="navigation">
          <Link to="/" className="nav-link">← Go to Save Page</Link>
        </div>
      </div>
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<SavePage />} />
          <Route path="/show" element={<ShowPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;