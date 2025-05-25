const { spawn } = require('child_process');
const path = require('path');

async function runPython(command, args) {
  return new Promise((resolve, reject) => {
    const py = spawn('python', [
      path.join(__dirname, '../py/cli.py'), 
      command, 
      ...args
    ]);
    
    let output = '';
    py.stdout.on('data', data => output += data);
    py.stderr.on('data', data => console.error(data.toString()));
    
    py.on('close', code => {
      if (code !== 0) reject(`Python error: ${output}`);
      else resolve(JSON.parse(output));
    });
  });
}

module.exports = { runPython };
