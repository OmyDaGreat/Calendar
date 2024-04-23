// getFestivals.js
import { exec } from 'child_process';

export async function handler(event, context) {
    return new Promise((resolve, reject) => {
        exec('python3 festivals.py', (error, stdout, stderr) => {
            if (error) {
                console.log(`error: ${error.message}`);
                return;
            }
            if (stderr) {
                console.log(`stderr: ${stderr}`);
                return;
            }
            resolve({
                statusCode: 200,
                body: stdout
            });
        });
    });
}
