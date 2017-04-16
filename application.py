from flask import Flask, render_template
from app import app

application = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/test/<username>')
# def index(username):
#     return render_template("index.html",
#                            title='Home',
#                            user=username)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
