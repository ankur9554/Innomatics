#import flask
from flask import Flask, request, url_for
from markupsafe import escape


#create app
app = Flask(__name__)
@app.route("/")
def home():
    return 'Welcome to home page!'
@app.route("/search")
def search():
    return 'Welcome to Search Page!'

@app.route("/upper_case")
def upper_case():
    string = request.args.get('string')
    string = str(string)
    string = string.upper()
    return string
@app.route("/add")
def sum():
    a= int((request.args.get('a')))
    b= int((request.args.get('b')))
    c = a+b
    return str(c)

    
if(__name__ == "__main__"):
    app.run(debug=True)






