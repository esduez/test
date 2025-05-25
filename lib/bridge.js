const { spawn } = require('child_process');

function runPython(command, args) {
  return new Promise((resolve, reject) => {
    const py = spawn('python', ['py/cli.py', command, ...args]);
    
    let result = '';
    py.stdout.on('data', data => result += data);
    py.stderr.on('data', data => console.error(data.toString()));
    
    py.on('close', code => code === 0 ? resolve(result) : reject(result));
  });
}

module.exports = { runPython };
