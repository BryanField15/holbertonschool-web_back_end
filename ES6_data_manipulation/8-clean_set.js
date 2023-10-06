function cleanSet(set, startString) {
  if (startString === '' || startString === null || typeof startString !== 'string') {
    return '';
  }
  const result = [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');

  return result;
}

export default cleanSet;
