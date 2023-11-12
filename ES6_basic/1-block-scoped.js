export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    let task = true;   // Use let for block-scoped variables
    let task2 = false;
  }

  return [task, task2];
}
