import "../../styles/side-bar.css";
import {Link} from 'react-router-dom'
function SideBar() {
  return (
    <>
      <div className="side-bar-wrapper">
        <div className="side-bar-top-height">

        </div>
          <ul className="side-bar-list">
            <li><Link to="/details"className="sidebar-link">Details</Link></li>
            <li><Link className="sidebar-link">Analytics</Link></li>
          </ul>
      </div>
    </>
  );
}

export default SideBar;
