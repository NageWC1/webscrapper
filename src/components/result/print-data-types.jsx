import React from "react";

function PrintDataType({ data }) {
  console.log("called");
  if (!data || data.length === 0) {
    console.log("nothing to print");
    return <div>No data to display</div>;
  }

  return (
    <div>
      <table className="table">
      <thead>
        <tr>
          <th>Column Name</th>
          <th>Data Type</th>
        </tr>
      </thead>
      <tbody>
        {data.map((row, index) => (
          <tr key={index}>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
          </tr>
        ))}
      </tbody>
    </table>
    </div>
  );
}

export default PrintDataType;
