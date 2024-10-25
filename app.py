from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "test"

@app.route('/trigger')
def trigger():
    return {"status": True}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
