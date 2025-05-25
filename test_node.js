const assert = require('assert');
const { runPython } = require('../lib/bridge');

describe('Python Bridge', () => {
  it('should return valid JSON', async () => {
    const result = await runPython('analyze', ['flask']);
    assert.doesNotThrow(() => JSON.parse(result));
  });
});
