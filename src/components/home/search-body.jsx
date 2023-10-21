import "../../styles/side-bar.css";
import { useState, useEffect } from "react";
function SearchBody() {
  const [link, setInitialData] = useState([{}]);
  const [Data_table, setTable] = useState({__html: ""});

  useEffect(() => {
    getTable()
  },[]);

  const getTable =(link) =>{
    var responseClone; // 1
    // let check with the table and see how its working 
    // https://www.youtube.com/watch?v=msEmUtYqVV0
    
  }
  
  return (
    <>
      <div className="search-body-wrapper">
        <form>
          <input
            placeholder="Enter the web link.... https://www/example.com"
            className="search-element"
            name="link"
            onChange={(e)=>setInitialData(e.target.value)}
          />
          <button className="search-btn"  onClick={getTable}>Get - a</button>
        </form>

        <div className="custom-gap"></div>
        <div>
          <div>
         {/* {Data_table} */}
          </div>
          
        </div>
      </div>
    </>
  );
}

export default SearchBody;
