# DevPSU Activity 

from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
        return "Fuck this Git shit I have never been more confused in my life"

if __name__ == "__main__":
    app.run()