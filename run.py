from flask import Flask

app = Flask(__name__)

@app.route('/')
def homePage():
    return{
        'test':'hi'
    }

@app.route('/contact')
def contactPage():
    return{
        'yo':[
            'shoha', 'brandt', 'aubrey'
        ]
    }

@app.route('/test')
def test():
    return  {
        'hello':'world'
    }

app.run()
