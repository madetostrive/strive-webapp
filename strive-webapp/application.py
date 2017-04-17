from flask import Flask
from flask import render_template

# Location is /opt/python/bundle/4/app/
# run db deploy from inside strive-webapp

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/')
def random():
    name = 'My Name'
    return render_template('index.html', name=name)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
