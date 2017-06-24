"""
所有的Flask程序都必须先创建一个Flask实例对象，
该实例对象用于处理来自客户端的所用请求，是Flask
程序的入口。
通常如下进行实例化：
"""

from flask import Flask#导入Flask类
app = Flask(__name__)#实例对象app,Flask类的构造函数必须传入一个指定的参数__name__

"""
路由和视图函数
路由衔接着用户请求的URL与视图函数之间的对应关系
视图函数则处理用户请求并做出响应
"""
@app.route("/")#路由
def index():#视图函数
    return "Hello,Welcome to HomePage create by Flask Framework."#具体响应

"""
动态参数与路由
动态参数能够实现个性化响应，动态参数部分写在<>内
凡是能够与路由中静态部分的URL相匹配的地址都将转交到该路由
"""
@app.route("/welcomeSomeone/<username>")
def welcomeSomeone(username):
    return "Hello,Welcome %s ." % username

'''
静态部分相同的URL，应具有不同的视图函数，否则出现复写错误，例如这个例子就不能够正常运行
@app.route('/welcomeSomeone')
def welcomeSomeone():
    return "welcome"
'''

'''
启动服务器：Flask自带服务器，开启debug模式，方便调试。

'''
#if __name__ == "__main__":
#    app.run(debug=True)

