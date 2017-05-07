#coding:utf-8
from flask import Flask,Response
app = Flask(__name__)

@app.route("/")
def hello():
    # return "Hello World!"
    f = file('/Users/scott/temp/a.png')
    f = file('/Users/scott/temp/evil_face.jpg')
    return Response(f.read(),mimetype='image/jpeg')

if __name__ == "__main__":
    app.run()