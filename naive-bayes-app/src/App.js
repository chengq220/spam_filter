import './App.css';
import React, { useState, useEffect } from 'react';
import axios from "axios";
import { API_URL } from "./environment/index";

function App() {
  const [spamState, setSpamState]  = useState("Enter something in the text below to check if it is a spam or not!")

  function predict(message){
    // console.log("function is getting called")
    if(document.getElementById('message').value.trim() === "") {
      alert("Input should not be empty");
    }else{
      setTimeout(ProgressBar(), 1000);
      axios.post(API_URL, message).then(response => {
        // console.log(response.data)
        if(response.data === 1){
          var bodyElement = document.querySelector('body');
          bodyElement.style.backgroundColor = "red";
          setSpamState("The message is likely a spam message");
          setTimeout(() => {bodyElement.style.backgroundColor = "#ffffff"}, 1500);
        }else{
          var bodyElement = document.querySelector('body');
          bodyElement.style.backgroundColor = "green";
          setSpamState("The message is unlikely a spam message");
          setTimeout(() => {bodyElement.style.backgroundColor = "#ffffff"}, 1500);
        }
        document.querySelector('#message').value = "Enter text here";
      }).catch(error => {
        // Handle errors if the request fails
        console.error('Error sending data to backend:', error);
      });
    }
    console.log("finish executing")
  }

  function ProgressBar(){
    var bar = document.querySelector(".progressBar");

    var width = 0;
    var increment = 1; // Adjust the increment value based on your preference
    var intervalTime = 10; // Interval time in milliseconds

    var id = setInterval(() => {
      if (width >= 100) {
        clearInterval(id);
      } else {
        width += increment;
        bar.style.width = width + '%';
      }
    }, intervalTime);
  }

  function clear(){
    document.querySelector(".progressBar").style.width = "0%";
    document.querySelector('#message').value = "Enter text here";
  }

  return (
    <div className="App">
      <div className="progressBar"></div>
      <div className="container">
        <div className="mainBody">
          <div className="classification">
            <p>{spamState}</p>
          </div>
          <div className="form_body">
            <textarea  type="text" id="message" name="message" placeholder="Enter text here"></textarea >
            <div className = "buttonContainer">
              <div id="submit" onClick= {() => predict(document.getElementById('message').value)}>Verify</div>
              <div id="clear" onClick = {() => clear()}>Clear</div>
            </div>
          </div>
          </div>
      </div>
    </div>
  );
}


export default App;
