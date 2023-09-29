import "../../styles/side-bar.css";
function SearchBody() {
  return (
    <>
      <div className="search-body-wrapper">
          <input
            placeholder="Enter the web link.... https://www/example.com"
            className="search-element"
          />
          <button className="search-btn">Get</button>
        </div>
    </>
  );
}

export default SearchBody;
