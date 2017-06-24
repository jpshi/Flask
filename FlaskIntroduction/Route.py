from flask import Flask#导入Flask类
app = Flask(__name__)#实例对象app



@app.route("/")
def index():
    return "test"
