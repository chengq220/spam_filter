import './App.css';
import React, { useState } from 'react';
import axios from "axios";
import { API_URL } from "./environment/index";

function App() {
  const [spamState, setSpamState]  = useState("Enter something in the text below to check if it is a spam or not!")

  function myFunc(message){
    console.log("function is getting called")
    if(document.getElementById('message').value.trim() === "") {
      alert("Input should not be empty");
    }else{
      axios.post(API_URL, message).then(response => {
        // console.log(response.data)
        if(response.data === 1){
          setSpamState("The message is likely a spam message")
        }else{
          setSpamState("The message is unlikely a spam message");
        }
      }).catch(error => {
        // Handle errors if the request fails
        console.error('Error sending data to backend:', error);
      });
    }
    console.log("finish executing")
  }

  return (
    <div className="App">
      <div className="container">
        <div className="classification">
          <p>{spamState}</p>
        </div>
        <div className="form_body">
          <input type="text" id="message" name="message" placeholder="Enter the text here"></input>
          <div id="submit" onClick= {() => myFunc(document.getElementById('message').value)}>Send</div>
        </div>
      </div>
    </div>
  );
}


export default App;
