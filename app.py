from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/greeting')
def greeting():
    py_name = request.form.get('form_name')
    return render_template('greetings.html',template_name=py_name)

@app.post('/square')
def square():
    py_num = request.form.get('num',0, type=int)
    print(py_num)
    square = py_num * py_num
    return render_template('square.html',num=py_num, square_num=square)
 