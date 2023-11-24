/*class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
  def add_to_tail(self, value):
    on = self
    while on.next:
      on = on.next
    on.next = Node(value)
  
  def get_at_index(self, index):
    on = self
    while on and index:
      on = on.next
      index = index - 1
    if on:
      return on.value
    else:
      return False
      
  def delete_by_value(self, value):
    on = self
    while on and on.next:
      if on.next.value == value:
        on.next = on.next.next
      on = on.next    
      
    
  def print_list(self):
    on = self
    while on:
      print(on.value, end="->")
      on = on.next
      
first_node = Node(1)
first_node.add_to_tail(2)
first_node.add_to_tail(3)
first_node.add_to_tail(4)
first_node.add_to_tail(5)

print(first_node.get_at_index(4))

#first_node.delete_by_value(3)

first_node.print_list()*/



/*process.stdin.resume();

process.on('SIGINT', function(){
  console.log("Got SIGINT. Press Control-D to exit.")
})*/

/*process.stdin.setEncoding('utf8')
process.stdin.on('readable', function() {
  var chunk = process.stdin.read();
  if (chunk !== null) {
    process.stdout.write('data: ' +chunk);
  }
});
process.stdin.on('end', function() {
  process.stdin.on('end');
});*/


// print process.argv
process.argv.forEach(function(val, index, array){
  console.log(index + ": " + val)
});