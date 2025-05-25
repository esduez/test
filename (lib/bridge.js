const { spawn } = require('child_process');

async function runPython(command, args = []) {
  return new Promise((resolve, reject) => {
    const python = spawn('python', ['py/cli.py', command, ...args]);
    
    let result = '';
    python.stdout.on('data', data => result += data);
    python.stderr.on('data', data => console.error(data.toString()));
    
    python.on('close', code => {
      if (code !== 0) reject(`Python exited with code ${code}`);
      else resolve(result.trim());
    });
  });
}

// Kullanım örneği
runPython('analyze', ['flask'])
  .then(console.log)
  .catch(console.error);
