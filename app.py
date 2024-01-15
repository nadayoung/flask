from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True) # 설정한 port를 지정할 수 있다
