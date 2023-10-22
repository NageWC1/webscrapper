import React from 'react';
import csvF from '../result/data.csv'
import excelF from '../result/data.xlsx'

function TableComponent({ data }) {
 console.log('called')
  if (!data || data.length === 0) {
    console.log("nothing to print")
    return <div>No data to display</div>;
  }

  // Assuming the first row in 'data' contains the headers
  const headers = data[0];

  return (
    <div>
      <span>To Download Cleaned CSV or Excel files of extracted table, click the buttons below</span>
      <div className='p-2 donwload-btn-wrapper'>
        
        <a href={csvF} download="data.csv"><button className='btn btn-success m-2'>Download CSV</button></a>
        <a href={excelF} download="data.xlsx"><button className='btn btn-primary m-2'>Download Excel</button></a>
      </div>
      <table className='table table-striped'>
        <thead className='thead-dark'>
          <tr>
            {headers.map((header, index) => (
              <th key={index}>{header}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.slice(1).map((row, rowIndex) => (
            <tr key={rowIndex}>
              {row.map((cell, cellIndex) => (
                <td key={cellIndex}>{cell}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TableComponent;
