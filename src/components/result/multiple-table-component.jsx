import React from "react";
import csvF from '../result/data.csv'
import excelF from '../result/data.xlsx'

function MultipleTableShow({ tables }) {
  return (
    <div>
      <div>
        {tables && tables.length > 0 ? (
          <div>
            <h2>Scraped Tables</h2>

            {tables.map((table, index) => (
              <div key={index}>
                <h3>Table {index + 1}</h3>
                <span className="description-text-for-download-buttns">
                  To Download Cleaned CSV or Excel files of extracted table,
                  click the buttons below
                </span>
                <div className="p-2 donwload-btn-wrapper">
                  <a href={csvF} download="data.csv">
                    <button className="btn btn-success m-2">
                      Download CSV
                    </button>
                  </a>
                  <a href={excelF} download="data.xlsx">
                    <button className="btn btn-primary m-2">
                      Download Excel
                    </button>
                  </a>
                </div>
                <table className="table table-striped">
                  <tbody>
                    {table.map((row, rowIndex) => (
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
        ) : null}
      </div>
    </div>
  );
}

export default MultipleTableShow;
