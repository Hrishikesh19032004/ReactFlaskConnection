import React, { useState, useEffect } from 'react';
import logo from './Accuracy.jpg';
import './App.css';

function App() {
  const [accuracy, setAccuracy] = useState(2);

  useEffect(() => {
    fetch("/api/ml")
      .then(res => {
        if (!res.ok) {
          throw new Error("Failed to fetch data");
        }
        return res.json();
      })
      .then(data => {
        console.log("API Data: ", data); // Add this to check the received data
        setAccuracy(data.accuracy);
      })
      .catch(err => {
        console.error("Error fetching accuracy:", err);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <div className="contain">
          <img src={logo} alt="logo" />
          <h2>Output: {accuracy}</h2>
        </div>
      </header>
    </div>
  );
}

export default App;
