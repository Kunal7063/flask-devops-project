import os
from flask import Flask

app = Flask(__name__)

MESSAGE = os.getenv("APP_MESSAGE", "Hello DevOps! Default message")

@app.route("/")
def home():
    #return "Hello DevOps! Feature branch update working."
     return MESSAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
