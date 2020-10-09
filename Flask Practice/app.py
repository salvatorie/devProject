# DevPSU Activity 

from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template("index.html")

@app.route('/hello/')
@app.route('/hello/<name>')
def helloName(name=None):
    return render_template("hello.html", name=name)

@app.route('/parks/')
def parks():
    with open('parks.json', 'r') as f:
        parks = json.load(f)
    
    return render_template("parks.html", parks=parks)

@app.route('/parks/name/')
def parksName():
    with open('parks.json', 'r') as f:
        parks = json.load(f)
    name = "name"
    return render_template("parks.html", parks=parks, name=name)


@app.route('/parks/loc/')
def parksLoc():
    with open('parks.json', 'r') as f:
        parks = json.load(f)
    loc = "loc"
    return render_template("parks.html", parks=parks, loc=loc)

@app.route('/parks/desc/')
def parksDesc():
    with open('parks.json', 'r') as f:
        parks = json.load(f)
    desc = "desc"
    return render_template("parks.html", parks=parks, desc=desc)

if __name__ == "__main__":
    app.run()