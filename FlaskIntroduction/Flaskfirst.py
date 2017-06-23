"""
所有的Flask程序都必须先创建一个Flask实例对象，
该实例对象用于处理来自客户端的所用请求，是Flask
程序的入口。
通常如下进行实例化：
"""

from flask import Flask#导入Flask类
app = Flask(__name__)#实例对象app,Flask类的构造函数必须传入一个指定的参数__name__

@app.route("/")
def index():
    return "Hello,Welcome to HomePage create by Flask Framework."

@app.route("/welcomeSomeone/<username>")
def welcomeSomeone(username):
    return "Hello,Welcome %s ." % username

if __name__ == "__main__":
    app.run(debug=True)

