import "../../styles/side-bar.css";
function SideBar() {
  return (
    <>
      <div className="side-bar-wrapper">
        <div className="side-bar-top-height">

        </div>
          <ul className="side-bar-list">
            <li><a>Details</a></li>
            <li><a>Analytics</a></li>
            <li><a>Download</a></li>
          </ul>
      </div>
    </>
  );
}

export default SideBar;
