// src/App.js
import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");

  const handleInputChange = (event) => {
    setQuestion(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const res = await axios.post("http://localhost:9000/query", {
        question: question,
      });
      setResponse(res.data.result);
    } catch (error) {
      console.error("Error querying the LLM:", error);
      setResponse("There was an error querying the LLM.");
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <form onSubmit={handleSubmit}>
          <label>
            Question:
            <input
              type="text"
              value={question}
              onChange={handleInputChange}
            />
          </label>
          <button type="submit">Submit</button>
        </form>
        {response && (
          <div className="response">
            <h2>Response:</h2>
            <p>{response}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
