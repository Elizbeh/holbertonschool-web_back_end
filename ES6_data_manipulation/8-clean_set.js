function cleanSet(set, startString) {
  return Array.from(set)
    .filter((element) => element.startsWith(startString))
    .map((element) => element.slice(startString.length))
    .join('-');
}

export default cleanSet;
