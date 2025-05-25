const { spawn } = require('child_process');
const path = require('path');
const logger = require('./logger');

async function runPythonScript(scriptName, args = []) {
    return new Promise((resolve, reject) => {
        const pythonProcess = spawn('python', [
            path.join(__dirname, `../py/${scriptName}.py`),
            ...args
        ]);

        let stdout = '';
        let stderr = '';

        pythonProcess.stdout.on('data', (data) => {
            stdout += data.toString();
        });

        pythonProcess.stderr.on('data', (data) => {
            stderr += data.toString();
        });

        pythonProcess.on('close', (code) => {
            if (code !== 0) {
                logger.error(`Python script exited with code ${code}: ${stderr}`);
                reject(new Error(stderr || 'Python script failed'));
            } else {
                try {
                    resolve(JSON.parse(stdout));
                } catch (e) {
                    logger.error('Failed to parse Python output:', stdout);
                    reject(e);
                }
            }
        });
    });
}

module.exports = {
    analyzePackage: (pkgName) => runPythonScript('cli', ['analyze', pkgName]),
    getTeaRewards: (userId) => runPythonScript('cli', ['rewards', userId])
};
