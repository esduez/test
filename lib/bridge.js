const { spawn } = require('child_process');
const path = require('path');

async function runPython(command, args) {
  const py = spawn('python', [
    path.join(__dirname, '../py/cli.py'), 
    command, 
    ...args
  ]);

  return new Promise((resolve, reject) => {
    let output = '';
    py.stdout.on('data', data => output += data);
    py.stderr.on('data', data => console.error(data.toString()));
    py.on('close', code => code === 0 ? resolve(output) : reject(output));
  });
}

module.exports = { runPython };
