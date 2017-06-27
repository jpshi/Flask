# -*- coding:utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
# Flask提供render_template方法将jinja2模板引擎集成到项目程序中
from flask import render_template 
from flask import session,url_for,redirect,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required,Length
import os

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
basedir = os.path.abspath(os.path.dirname(__name__))
print ("***"+basedir)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////' + os.path.join(basedir,'flasky.db')
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)



@app.route('/',methods=['GET','POST'])
def index():
    '''flash消息提醒'''
    form = NameForm()
    if form.validate_on_submit():
        oldname = session.get('name')#表单提交后浏览器通过session保持表单数据
        if oldname is not None and oldname != form.name.data:
            flash('用户发生了变更，请留心！！！')
        session['name'] = form.name.data    
        return redirect(url_for("index"))
    return render_template('index.html',form = form,name = session.get('name'))
    
@app.route('/user/<username>')
def user(username):
    #return render_template('user.html',name = username)#页面渲染过程，注意变量name必须与模板中的变量保持一致
    return render_template('bootstrapuser.html',username=username)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



class NameForm(FlaskForm):
    name = StringField('What is your name',validators=[Required()])
    pswd = PasswordField("Input your Password",validators=[Required(),Length(min=4)])
    submit = SubmitField('Submit')

class User(db.Model):
    #类的属性 相当于 数据库表中的字段
    userid = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(16),unique = True)
    email = db.Column(db.String(160),unique = True)
    # 类的属性 end

    #默认构造方法，方便调试和测试
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
    #end 默认构造方法

class Role(db.Model):
    roleid = db.Column(db.Integer,primary_key = True)
    rolename = db.Column(db.String(16),unique = True)

    def __init__(self,roleid,rolename):
        self.roleid = roleid
        self.rolename = rolename

    def __repr__(self):
        return '<Role %r>' % self.rolename

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)