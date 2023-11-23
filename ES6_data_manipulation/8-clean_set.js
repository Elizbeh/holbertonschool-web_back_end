function cleanSet(set, startString) {
  // check if startString is falsy or not a string
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  return Array.from(set)
    .filter((element) => element !== undefined && element.startsWith(startString))
    .map((element) => element.slice(startString.length))
    .join('-');
}

export default cleanSet;
