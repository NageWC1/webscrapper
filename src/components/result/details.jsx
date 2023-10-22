import React from "react";
import NavBar from "../home/nav";
import SideBar from "../home/side-bar";
import { useState, useEffect } from "react";
import axios from "axios";
import PrintDataType from "./print-data-types";

import "../../styles/print-table.css";
function Details() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/data_types")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        setData(data.data_types_list);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []); // The empty dependency array ensures this effect runs once on component mount

  return (
    <div >
      <NavBar />
      <div className="home-body">
        <SideBar />
        <div className="table-container">
          <PrintDataType data={data} />
        </div>
      </div>
    </div>
  );
}

export default Details;
