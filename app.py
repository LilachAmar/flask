from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return render_template("welcome_name.html", name=name)


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form['nm']
        return redirect(url_for("hello_name", name=user))
    if request.method == "GET":
        user = request.args.get('nm')
        return redirect(url_for("hello_name", name=user))

if __name__ == "__main__":
    app.run()
