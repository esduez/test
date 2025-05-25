const assert = require('assert');
const { analyzePackage } = require('../../lib/bridge');

describe('Python Bridge', function() {
    this.timeout(10000);

    it('should analyze package dependencies', async () => {
        const result = await analyzePackage('flask');
        assert.ok(Array.isArray(result.dependencies));
    });

    it('should handle invalid packages', async () => {
        try {
            await analyzePackage('invalid_package_123');
            assert.fail('Should have thrown error');
        } catch (e) {
            assert.ok(e instanceof Error);
        }
    });
});
