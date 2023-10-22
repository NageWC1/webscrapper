import "../../styles/side-bar.css";
import { useState, useEffect } from "react";
import apiServices from "../../api-services/api-services";
import TableComponent from "../result/table-component";
function SearchBody() {
  const [link, setLink] = useState('');
  const [tableData, setTableData] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleScrape = () => {
    setLoading(true);

    // Make a POST request to your Flask server with the link
    fetch('/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ link }),
    })
      .then((response) => response.json())
      .then((data) => {
        setTableData(data.row_data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
        setLoading(false);
      },[]);
  };
  return (
    <>
      <div className="search-body-wrapper">
        <form>
          <input
            placeholder="Enter the web link.... https://www/example.com"
            className="search-element"
            name="link"
            type="text"
            value={link}
            onChange={(e) => setLink(e.target.value)}
          />
          <button className="search-btn" onClick={handleScrape} disabled={loading}>
          {loading ? 'Scraping...' : 'Get'}
          </button>
        </form>

        <div className="custom-gap"></div>
        
        <div>
          <TableComponent data={tableData} />
        </div>
      </div>
    </>
  );
}

export default SearchBody;
