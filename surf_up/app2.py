from flask import Flask 
app = Flask(__name__) # Initiazlize the flask app

@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug = True)

# export FLASK_APP=app.py
# set FLASK_APP=app.py
# flask run