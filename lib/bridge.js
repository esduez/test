const { spawn } = require('child_process');
const path = require('path');

async function runPython(scriptName, args = []) {
    return new Promise((resolve, reject) => {
        const pythonProcess = spawn('python', [
            path.join(__dirname, `../py/${scriptName}.py`),
            ...args
        ]);

        let stdout = '';
        pythonProcess.stdout.on('data', (data) => stdout += data.toString());
        
        pythonProcess.on('close', (code) => {
            if (code !== 0) reject(new Error(`Python exited with code ${code}| ${stdout}`));
            else resolve(JSON.parse(stdout));
        });
    });
}

module.exports = {
    analyzePackage: (pkg) => runPython('cli', ['analyze', pkg]),
    getTeaRewards: (userId) => runPython('cli', ['rewards', userId])
};
