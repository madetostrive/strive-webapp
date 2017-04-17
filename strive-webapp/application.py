from flask import Flask
from flask import render_template

# Location is /opt/python/bundle/4/app/
# run db deploy from inside strive-webapp

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/think')
def think():
    return render_template('think.html')

@application.route('/choosing')
def choosing():
    return render_template('choosing.html')

@application.route('/finaid')
def finaid():
    return render_template('finaid.html')

@application.route('/testing')
def testing():
    return render_template('testing.html')

if __name__ == "__main__":
    application.debug = True
    application.run()
