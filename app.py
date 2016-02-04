from flask import Flask, render_template
from flask import request

app = Flask(__name__)
app.config["DEBUG"] = True # only include while testing 

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/name")
def name():
    return "Alexandre Lamy"

@app.route("/search")
def search():
    return render_template("search.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
