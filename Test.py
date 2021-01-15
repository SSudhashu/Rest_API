from flask import Flask,request,render_template



app = Flask(__name__)

@app.route('/')

def home():
    return "Hello!! <h1> Testing<h1>"

@app.route('/ok/<name>')

def greet(name):
    return "<br><h2>Hello Mr/Miss {}".format(name)


if __name__ == '__main__':
   app.run(debug = True)