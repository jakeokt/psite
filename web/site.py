
from flask import Flask, render_template, request, url_for, redirect, make_response, abort
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
                            

if __name__ == '__main__':
    app.run()