import "./App.css";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/home";

function App() {
  return (
    <>
      <Routes>
        {/* common page */}
        <Route path="/" element={<Home />} /> {/* home page */}
      </Routes>
    </>
  );
}

export default App;
