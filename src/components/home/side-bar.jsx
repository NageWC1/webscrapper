import "../../styles/side-bar.css";
function SideBar() {
  return (
    <>
      <div className="side-bar-wrapper">
        <div style={{height:'2vh'}}>

        </div>
          <ul className="side-bar-list">
            <li>Details</li>
            <li>Analytics</li>
            <li>Charts</li>
          </ul>
      </div>
    </>
  );
}

export default SideBar;
