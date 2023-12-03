// 0-calcul.test.js

var assert = require('assert');

const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should round and sum two numbers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4); // Expected value corrected from 3 to 4
  });

  it('should round and sum two numbers with decimals', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should round and sum two decimal numbers', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should round and sum two decimal numbers resulting in a higher integer', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should round and sum two negative decimal numbers', () => {
    assert.strictEqual(calculateNumber(-1.2, -3.7), -5);
  });

  it('should round and sum two decimal numbers resulting in a lower negative integer', () => {
    assert.strictEqual(calculateNumber(-1.5, -3.7), -5);
  });

  it('should round and sum a positive integer and a negative float', () => {
    assert.strictEqual(calculateNumber(1, -3.7), -3); 
  });

  it('should round and sum a negative integer and a positive float', () => {
    assert.strictEqual(calculateNumber(-1, 3.7), 3);
  });

  it('should round and sum two negative integers', () => {
    assert.strictEqual(calculateNumber(-1, -3), -4);
  });

  it('should round and sum a negative integer and a negative float', () => {
    assert.strictEqual(calculateNumber(-1, -3.7), -5);
  });

  it('should round and sum two negative decimal numbers', () => {
    assert.strictEqual(calculateNumber(-1.2, -3.7), -5);
  });

   it('should round and sum two decimal numbers resulting in a lower negative integer', () => {
    assert.strictEqual(calculateNumber(-1.5, -3.7), -5);
  });
});

