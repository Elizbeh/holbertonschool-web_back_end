const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  it('should round and add two numbers when type is SUM', () => {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.be.equal(6);
  });

  it('should round and subtract b from a when type is SUBTRACT', () => {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4); 
  });

  it('should round and divide a by b when type is DIVIDE', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.be.equal(0.2);
  });

  it('should return "Error: Division by zero is not allowed" when trying to divide by 0', () => {
    expect(() => calculateNumber('DIVIDE', 1.4, 0).to.equal(Error);
  });

  it('should round and add two positive integers when type is SUM', () => {
    expect(calculateNumber('SUM', 3, 5)).to.equal(8);
  });

  it('should round and subtract b from a when type is SUBTRACT for negative numbers', () => {
    expect(calculateNumber('SUBTRACT', -1.4, -4.5)).to.be.equal(3);
  });

  it('should round and divide a by b when type is DIVIDE for negative numbers', () => {
    expect(calculateNumber('DIVIDE', -1.4, 4.5)).to.be.equal(-0.2);
  });

  it('should round and add two decimal numbers when type is SUM', () => {
    expect(calculateNumber('SUM', 1.23, 4.56)).to.be.equal(6);
  });

  it('should round and subtract b from a when type is SUBTRACT for decimal numbers', () => {
    expect(calculateNumber('SUBTRACT', 7.89, 2.34)).to.equal(6);
  });

  it('should round and divide a by b when type is DIVIDE for decimal numbers', () => {
    expect(calculateNumber('DIVIDE', 8.64, 2.16)).to.be.equal(4.5);
  });

  it('should return "Error: Division by zero is not allowed" when trying to divide by 0 for decimal numbers', () => {
    expect(() => calculateNumber('DIVIDE', 5.5, 0).to.throw('Error: Division by zero is not allowed'));
  });

  it('should round and add two negative decimal numbers when type is SUM', () => {
    expect(calculateNumber('SUM', -1.23, -4.56)).to.be.equal(-6);
  });

  it('should round and subtract b from a when type is SUBTRACT for positive decimal numbers', () => {
    expect(calculateNumber('SUBTRACT', 7.89, 2.34)).to.be.equal(6);
  });

  it('should round and divide a by b when type is DIVIDE for positive decimal numbers', () => {
    expect(calculateNumber('DIVIDE', 8.64, 2.16)).to.be.equal(4.5);
  });

  it('should return "Error: Division by zero is not allowed" when trying to divide by 0 for negative decimal numbers', () => {
    expect(() => calculateNumber('DIVIDE', -5.5, 0).to.throw('Error: Division by zero is not allowed'));
  });

  it('should return "Error: Division by zero is not allowed" when trying to divide by 0 for zero values', () => {
    expect(() => calculateNumber('DIVIDE', 0, 0).to.throw('Error: Division by zero is not allowed'));
  });
});

