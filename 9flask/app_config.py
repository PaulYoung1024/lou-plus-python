from flask import Flask
app=Flask(__name__)

app.config.from_json('config.json')
app.config.update({
    'SECRET_KEY':'ypp'
    })

@app.route('/')
def index():
    return app.config['SECRET_KEY']
    #return app.config['USER_NAME']

if __name__=='__main__':
    app.run()
