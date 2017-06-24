'''
Flask调用视图函数后将其返回结果作为响应内容呈现给客户端，
通常情况下，响应内容为字符串,有时候为了获取请求状态，Flask允许返回值接受
除返回字符串、动态参数之外的第三个参数--状态码（Status Code）
状态码是一串数字代码，与前两个返回值之间用，隔开
状态码包括5类：
1××：信息
2××：成功
3××：重定向
4××：客户端错误/请求错误/无法完成请求
5××：服务器错误

常见的状态码有：
200:OK
301:Redict
403:Forbidden
404:Not found
500:Internal Server Erro
502:Bad Gateway
504:Gateway time-out
'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Homepage",200

@app.route("/404.html")
def Notfound():
    return "Not found",404

from flask import redirect    
@app.route("/redict")
def Redictor():
    return redirect("http://www.dangdang.com/")


if __name__ == "__main__":
    app.run(debug=True)
