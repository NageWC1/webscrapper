class apiServices {
  static getTable(link) {
    return fetch(`http:/127.0.0.1:5000/${link}`)
    .then(function (response) {
      // responseClone = response.clone(); // 2
      return response.html();
    })
  }
}

export default apiServices;
