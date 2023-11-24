//const obj1 = { 0: 1, 1: 2, 2: 3, length: 3 };
//const obj2 = { 0: 1, 1: 2, 2: 3, length: 3,
//[Symbol.isConcatSpreadable]: true};
//console.log([0].concat(obj1, obj2));


//console.log(Array.prototype.concat.call({}, 1, 2, 3))
//console.log(Array.prototype.concat.call(1, 2, 3))

/*const arrayLike = {
 [Symbol.isConcatSpreadable]: true,
 length: 2,
 0:1,
 1:2,
 2:3,
}
console.log(Array.prototype.concat.call(arrayLike, 3, 4))*/

/*const array1 = ['a', 'b', 'c', 'd', 'e'];
console.log(array1.copyWithin(0, 3, 4))
console.log(array1.copyWithin(1, 3))*/


//const map1 = new Map();
//map1.set('a', 1);
//map1.set('b', 2);
//map1.set('c', 3);
//console.log("------------")
//console.log(map1)
//console.log("------------")
//console.log(map1.get("a"))
//console.log("------------")
//console.log(map1.size)


//const contacts = new Map()
//contacts.set("Jessie", {phone: "213-555-1234", address: "123 N 1st Ave" });
//contacts.has("Jessie");
//contacts.get("Hilary");
//contacts.set("Hilary", { phone: "617-555-4321", address: "321 S 2nd St" });
//contacts.get("Jessie"); // {phone: "213-555-1234", address: "123 N 1st Ave"}
//contacts.delete("Raymond"); // false
//contacts.delete("Jessie"); // true
//console.log(contacts.size); // 1


// typed Array
//const uint8 = new Uint8Array([1, 2, 3]);
//console.log(uint8[0])

/*class Node {
  constructor(value) {
    this.value = value
    this.next = null 
  }
}

const node1 = new Node(4)
console.log(node1)*/

/*function isBigEnogh(element, index, array) {
  return element >= 10;
}

console.log([12, 5, 8, 130, 44].every(isBigEnogh));
console.log([12, 54, 18, 130, 44].every(isBigEnogh));*/


const http = require('http');

const hostname = '127.0.0.1';

const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200
  res.setHeader('Content-Type', 'text/plain')
  res.end('Hello you! Welcome')
})

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}`)
})

