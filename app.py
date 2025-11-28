from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask app Practice done and last and final update again testing mail is having problem one more"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
