from flask import Flask,url_for,redirect
app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/user/<username>')
def index_user(username):
    return 'Hello {}'.format(username)

@app.route('/courses/<name>')
def courses(name):
    return 'Courses:{}'.format(name)

@app.route('/test')
def test():
    print(url_for('courses',name='java',_external=True))
    return redirect(url_for('index_user',username='yangpingping'))

if __name__=='__main__':
    app.run()
