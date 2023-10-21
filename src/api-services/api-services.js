class apiServices {
  static getTable(link) {
    return fetch(`http:/127.0.0.1:5000/${link}`)
    .then(function (response) {
      responseClone = response.clone(); // 2
      return response.json();
    })
    .then(
      function (data) {
        setTable(data)
        console.log(data)
      },
      function (rejectionReason) {
        // 3
        console.log(
          "Error parsing JSON from response:",
          rejectionReason,
          responseClone
        ); // 4
        responseClone
          .text() // 5
          .then(function (bodyText) {
            console.log(
              "Received the following instead of valid JSON:",
              bodyText
            ); // 6
          });
      }
    );
  }
}

export default apiServices;
