function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Data from API'); // Resolving the promise after 2 seconds
    }, 2000);
  });
}

export default getResponseFromAPI;
