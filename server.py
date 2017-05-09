from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'my_secret_key'


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)