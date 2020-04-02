from flask import Flask ,render_template 

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1> Homepage <h1>"

@app.route("/list")
def lst():
    return render_template("list.html")

@app.route("/kitchen")
def kitchen():
    return render_template("kitchen.html")

@app.route("/winner/<name>")
def winner(name):
    name = name.capitalize()
    return render_template("name.html",name = name)

