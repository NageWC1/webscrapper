import "../../styles/side-bar.css";
import { useState, useEffect } from "react";
function SearchBody() {
  const [initialData, setInitialData] = useState([{}]);

  useEffect(() => {
    var responseClone; // 1
    fetch("/api")
      .then(function (response) {
        responseClone = response.clone(); // 2
        return response.json();
      })
      .then(
        function (data) {
          setInitialData(data)
        },
        function (rejectionReason) {
          // 3
          console.log(
            "Error parsing JSON from response:",
            rejectionReason,
            responseClone
          ); // 4
          responseClone
            .text() // 5
            .then(function (bodyText) {
              console.log(
                "Received the following instead of valid JSON:",
                bodyText
              ); // 6
            });
        }
      );
  },[]);

  
  return (
    <>
      <div className="search-body-wrapper">
        <form action="/" method="post">
          <input
            placeholder="Enter the web link.... https://www/example.com"
            className="search-element"
            name="link"
          />
          <button className="search-btn" type="submit" value="sumbmit">Get - a</button>
        </form>

        <div className="custom-gap"></div>
        <div>
          {(typeof initialData.member === "undefined")?(
          <h1>Data Loading</h1>
          ):(
              <span className="result-text">{initialData} </span>
          )}
          
        </div>
      </div>
    </>
  );
}

export default SearchBody;
