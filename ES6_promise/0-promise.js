function getResponseFromAPI(){
  return new Promise((resolve, reject) =>{
    const responseApi = {data: "Data fetched"}
    if (responseApi) {
      resolve(responseApi)
    }else{
      reject(new Error("Processing Failed"))
    }
  })
}