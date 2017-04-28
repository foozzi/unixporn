from flask import Flask, render_template, redirect, request
from flask_assets import Environment, Bundle
app = Flask(__name__, template_folder="views")


assets = Environment(app)

#main css packed 
main_css = Bundle('css/bootstrap/bootstrap.min.css', 'css/main.css',
    filters='cssmin', output='gen/packed_main.css')
assets.register('main_css', main_css)

main_js = Bundle('js/bootstrap/bootstrap.min.js',
    filters='jsmin', output='gen/packed_main.js')
assets.register('main_js', main_js)

# Import Controllers
from controllers.main import Main
main = Main()

# Routes
@app.route('/')
def welcomeIndex():
    return main.index()

# Run Server
app.run(debug=True)
