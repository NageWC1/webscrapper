import NavBar from "../components/home/nav";
import SearchBody from "../components/home/search-body";
import SideBar from "../components/home/side-bar";
import "../styles/home.css"
function Home() {
  return (
    <>
      <NavBar />
      <div className="home-body">
        <SideBar />
        <SearchBody />
      </div>
    </>
  );
}

export default Home;
