from flask import Flask
app = Flask(__name__)


from flask import render_template # Flask提供render_template方法将jinja2模板引擎集成到项目程序中
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def user(username):
    return render_template('user.html',name = username)#页面渲染过程，注意变量name必须与模板中的变量保持一致

if __name__ == '__main__':
    app.run(debug = True)