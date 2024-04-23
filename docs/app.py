from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/run-main')
def run_main():
    # Run the main.py script
    subprocess.run(['python', 'main.py'])
    return "Python script executed."

if __name__ == '__main__':
    app.run(debug=True)
