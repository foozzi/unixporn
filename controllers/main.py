from flask import Flask, render_template, redirect, request
from models.user import User

class Main:
    """Main Controller"""

    def index(app):                
        return render_template("index.html")

    def sign_up(app):
        return render_template('sign_up.html')
