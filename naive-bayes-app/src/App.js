import './App.css';
import React, { useState } from 'react';

function App() {
  const [spamState, setSpamState]  = useState("Enter something in the text below to check if it is a spam or not!")

  function myFunc(message){
    if(document.getElementById('message').value.trim() === "") {
      alert("Input should not be empty");
    }else{
      var isSpam = false
      if(isSpam){
        setSpamState("The message is likely a spam message");
      }else{
        setSpamState("The message is unlikely a spam message");
      }
    }
  }

  return (
    <div className="App">
      <table className="container">
        <tr className="classification">
          <p>{spamState}</p>
        </tr>
        <tr className="form_body">
          <input type="text" id="message" name="message" placeholder="Enter the text here"></input>
          <button onClick= {() => myFunc(document.getElementById('message').value)}>Check</button>
        </tr>
      </table>
    </div>
  );
}


export default App;
