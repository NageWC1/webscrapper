import "../../styles/nav.css";
function NavBar() {
  return (
    <>
      <div className="nav-wrapper">
        <div className="brand-log-text">
          <span style={{ color: "red" }}>W</span>
          <span>eb</span>
          <span style={{ color: "red" }}> S</span>
          <span>crapper 🌐</span>
        </div>
        <div className="nav-links-wrapper">
          <ul>
            <li>Home</li>
            <li>About</li>
            <li>Service</li>
          </ul>
        </div>
      </div>
    </>
  );
}

export default NavBar;
