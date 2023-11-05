import React from "react";
import NavBar from "../home/nav";
import SideBar from "../home/side-bar";
import { useState, useEffect } from "react";
import axios from "axios";
import PrintDataType from "./print-data-types";

import "../../styles/print-table.css";
function Details() {
  const [data, setData] = useState([]);
  const [analyzedTables, setAnalyzedTables] = useState([]);

  useEffect(() => {
    fetch("/identify_data_types")
      .then((response) => response.json())
      .then((data) => {
        setAnalyzedTables(data.analyzed_tables);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <div>
      <NavBar />
      <div className="home-body">
        <SideBar />
        <div className="table-container">
          <div>
            {analyzedTables.map((table, index) => (
              <div key={index}>
                <h2>Table {index + 1}</h2>
                <table className="table table-dark table-hover">
                  <thead>
                    {table[0].map((header, headerIndex) => (
                      <th key={headerIndex}>{header}</th>
                    ))}
                  </thead>
                  <tbody>
                    {table.slice(1).map((row, rowIndex) => (
                      <tr key={rowIndex}>
                        {row.map((cell, cellIndex) => (
                          <td key={cellIndex}>{cell}</td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Details;
