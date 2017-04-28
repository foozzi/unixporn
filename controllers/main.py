from flask import Flask, render_template, redirect, request

class Main:
    """Main Controller"""

    def index(app):                
        return render_template("index.html")
