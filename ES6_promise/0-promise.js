function getResponseFromAPI(){
  return new Promise((resolve, reject) => {
    //Simulating an asyncronous API call
    setTimeout(() => {
      const responseApi = {data:"Data retrival successful"};
      if (responseApi) {
        resolve(responseApi);
      }else{
        reject(new Error("Failed to retrieve data"));
      }
    }, 1000); // 1 second delay
  });
}