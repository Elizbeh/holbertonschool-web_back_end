function hasValuesFromArray(set, array) {
  // Every method check if all elements in the array exist in the set
  return array.every((value) => set.has(value));
}

export default hasValuesFromArray;
