const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('should round and add two numbers when type is SUM', () => {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });

  it('should round and subtract b from a when type is SUBTRACT', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });

  it('should round and divide a by b when type is DIVIDE', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });

  it('should return Error: Division by zero is not allowed', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error:');
  });

  it('should round and add two positive integers when type is SUM', () => {
    assert.strictEqual(calculateNumber('SUM', 3, 5), 8);
  });

  it('should round and subtract b from a when type is SUBTRACT for negative numbers', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -4.5), 3);
  });

  it('should round and divide a by b when type is DIVIDE for negative numbers', () => {
    assert.strictEqual(calculateNumber('DIVIDE', -1.4, 4.5), -0.2);
  });

  it('should round and add two decimal numbers when type is SUM', () => {
    assert.strictEqual(calculateNumber('SUM', 1.23, 4.56), 6);
  });

  it('should round and subtract b from a when type is SUBTRACT for decimal numbers', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 7.89, 2.34), 6);
  });

  it('should round and divide a by b when type is DIVIDE for decimal numbers', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 5, 1.2), 5);
  });

  it('should return "Error: Division by zero is not allowed" when trying to divide by 0 for decimal numbers', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 5.5, 0), 'Error:');
  });

  it('should round and add two negative decimal numbers when type is SUM', () => {
    assert.strictEqual(calculateNumber('SUM', -1.23, -4.56), -6);
  });

  it('should round and subtract b from a when type is SUBTRACT for positive decimal numbers', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 7.89, 2.34), 6);
  });

  it('should return "Error: Division by zero is not allowed" when trying to divide by 0 for negative decimal numbers', () => {
    assert.strictEqual(calculateNumber('DIVIDE', -5.5, 0), 'Error:');
  });

  it('should round and add two zero values when type is SUM', () => {
    assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
  });

  it('should round and subtract b from a when type is SUBTRACT for zero values', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 0, 0), 0);
  });

  it('should return "Error: Division by zero is not allowed" when trying to divide by 0 for zero values', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error:');
  });
});

