# DevPSU Activity 

from flask import Flask, render_template

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
    parks = ['Yellowstone', "Yosemite", "Glacier"]

    return render_template("parks.html", parks=parks)

if __name__ == "__main__":
    app.run()