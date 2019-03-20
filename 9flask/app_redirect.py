from flask import Flask,url_for,redirect

app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/<username>')
def hello(username):
    if username=='yangpingping':
        return 'hello {}'.format(username)
    else:
        #return redirect(url_for('index'))
        return redirect('/')
