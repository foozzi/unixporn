from flask import Flask, render_template, redirect, request
app = Flask(__name__, template_folder="views")

# Import Controllers
from controllers.main import Main
main = Main()

# Routes
@app.route('/')
def welcomeIndex():
    return main.index()

@app.route('/sign_up')
def signUp():
    return main.sign_up()

