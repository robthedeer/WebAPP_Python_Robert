from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    user ={'username': 'admin', 'password': '123456'}
    return '''<html>
    <head> 
    <title>Home Page - QES School</title>
    </head>
    <body> 
    <h1>Hello,'''+ user['username'] +'''</h1>
    </body>
    </html>'''
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)