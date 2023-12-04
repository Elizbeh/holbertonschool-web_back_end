const calculateNumber = (type, a, b) => {
  const firstArg = Math.round(a);
  const secondArg = Math.round(b);

  switch(type) {
    case 'SUM':
      return firstArg + secondArg;
    case 'SUBTRACT':
      return firstArg - secondArg;
    case 'DIVIDE':
      return (secondArg === 0) ? 'Error:' : firstArg / secondArg;
    default:
      throw new Error('Type argument only accept SUM, SUBSTRACT, or DIVIDE');
  }
};

module.exports = calculateNumber;
