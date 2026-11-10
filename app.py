from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

#Connection à MongoDB
client = MongoClient("mongodb://mongo:27017/")
database = client["ex5Flask"]


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)
