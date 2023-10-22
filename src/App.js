import "./App.css";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/home";
import Details from "./components/result/details";

function App() {
  return (
    <>
      <Routes>
        {/* common page */}
        <Route path="/" element={<Home />} /> {/* home page */}
        <Route path="/details" element={<Details />} /> {/* home page */}
      </Routes>
    </>
  );
}

export default App;
