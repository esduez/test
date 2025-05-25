const assert = require('assert');
const { analyzePackage } = require('../../lib/bridge');

describe('Python Bridge', function() {
    this.timeout(10000);

    it('should return package info', async () => {
        const result = await analyzePackage('flask');
        assert.ok(Array.isArray(result.dependencies));
    });
});
