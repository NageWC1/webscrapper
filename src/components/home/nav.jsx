import "../../styles/nav.css";
import "../../styles/nav-responsiveness.css";
import {Link} from'react-router-dom'
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
              <li><Link to="/"className="sidebar-link">Home</Link></li>
              <li><Link to="/details"className="sidebar-link">About</Link></li>
              <li><Link to="/details"className="sidebar-link">Service</Link></li>
          </ul>
        </div>
      </div>
    </>
  );
}

export default NavBar;
