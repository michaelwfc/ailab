"""
@author: michaelwfc
@version: 1.0.0
@license: Apache Licence
@file: hello_template.py
@time: 2023/9/5 0:08
"""

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # flask通过render_template()函数来实现模板的渲染。和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是jinja2

    return render_template(r'home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template(r'form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template(r'signin-ok.html', username=username)
    return render_template(r'form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
