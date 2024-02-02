from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greeting', methods=['POST'])
def greeting():
    py_name = request.form.get('form_name')
    return render_template('greetings.html',template_name=py_name)
 