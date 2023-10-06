function cleanSet(set, startString) {
  if (startString === '' || startString === null || typeof startString !== 'string') {
    return '';
  }

  const result = [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => {
      if (value === startString) return value.slice(startString.length);
      return value.replace(startString, '');
    })
    .join('-');

  return result;
}

export default cleanSet;
