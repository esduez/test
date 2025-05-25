const assert = require('assert');
const { runPython } = require('../../lib/bridge');

describe('Python Bridge', () => {
  it('should return package info', async () => {
    const result = await runPython('analyze', ['flask']);
    assert.ok(result.dependencies);
  });
});
