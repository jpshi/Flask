# -*- coding:utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

bootstrap = Bootstrap(app)

# Flask提供render_template方法将jinja2模板引擎集成到项目程序中
from flask import render_template 
from flask import session,url_for,redirect


@app.route('/',methods=['GET','POST'])
def index():
    '''通过使用重定向和session技术解决重复提交表单问题'''
    form = NameForm()
    if form.validate_on_submit():
        session['name']=form.name.data
        return redirect('/')
    return render_template('index.html',form = form,name = session.get('name'))
    
@app.route('/user/<username>')
def user(username):
    #return render_template('user.html',name = username)#页面渲染过程，注意变量name必须与模板中的变量保持一致
    return render_template('bootstrapuser.html',username=username)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required,Length

class NameForm(FlaskForm):
    name = StringField('What is your name',validators=[Required()])
    pswd = PasswordField("Input your Password",validators=[Required(),Length(min=4)])
    submit = SubmitField('Submit')

if __name__ == '__main__':
    app.run(debug = True)