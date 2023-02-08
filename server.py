from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__)
app.secret_key = "Don't you wanna know?!?!?"


def sumSessionCounter():
    if 'visited' in session:
        session['visited'] += 1
    else:
        session['visited'] = 1
    return


@app.route('/')
def index():
    sumSessionCounter()
    print(session['visited'])
    return render_template("index.html")

@app.route('/count')
def count():
    print("Person has been here!")
    sumSessionCounter()
    return redirect('/')


@app.route('/destroy_session')
def restart():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
