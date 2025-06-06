import React, { useState } from "react";
import "./App.css";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

// Local storage key for storing the number
const STORAGE_KEY = "savedNumber";

// Page 1: Save Number
const SavePage = () => {
  const [number, setNumber] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleSave = () => {
    if (!number.trim()) {
      setMessage("Please enter a number");
      return;
    }

    const numValue = parseFloat(number);
    if (isNaN(numValue)) {
      setMessage("Please enter a valid number");
      return;
    }

    setLoading(true);
    setMessage("");

    // Simulate loading delay for better UX
    setTimeout(() => {
      try {
        // Save to localStorage
        localStorage.setItem(STORAGE_KEY, numValue.toString());
        setMessage(`Number ${numValue} saved successfully!`);
        setNumber("");
      } catch (error) {
        console.error("Error saving number:", error);
        setMessage("Error saving number. Please try again.");
      } finally {
        setLoading(false);
      }
    }, 300);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSave();
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
            onKeyPress={handleKeyPress}
            placeholder="Enter a number"
            className="number-input"
            step="any"
          />
          <button 
            onClick={handleSave} 
            disabled={loading}
            className="save-btn"
          >
            {loading ? "Saving..." : "Save"}
          </button>
        </div>
        {message && <p className={`message ${message.includes('Error') ? 'error' : ''}`}>{message}</p>}
        
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

  const handleShow = () => {
    setLoading(true);
    
    // Simulate loading delay for better UX
    setTimeout(() => {
      try {
        // Get from localStorage
        const storedNumber = localStorage.getItem(STORAGE_KEY);
        
        if (storedNumber !== null) {
          setSavedNumber(parseFloat(storedNumber));
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
    }, 300);
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
          {loading ? (
            <p className="loading">Loading...</p>
          ) : savedNumber !== null ? (
            <p className="number-display">
              Last saved number: <span className="number">{savedNumber}</span>
            </p>
          ) : hasNumber === false && savedNumber === null ? (
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

// Home component that redirects to SavePage
const Home = () => {
  return <SavePage />;
};

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/save" element={<SavePage />} />
          <Route path="/show" element={<ShowPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;