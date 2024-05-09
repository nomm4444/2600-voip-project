from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<p>Welcome to the site. You are free to:</p>
    <ul>
        <li>watch aout the alerts in real time at <a href="http://127.0.0.1:5000/alerts">/alerts</a></li>
        <li>Check out the probe at <a href='http://127.0.0.1:5000/probe'>/probe</a></li>
        <li>upload the CSV for the CDR at <a href='http://127.0.0.1:5000/upload'>/upload</a></li>
    </ul>"""

@app.route("/alerts")
def alerts():
    return "<p>welcome to real time alerts!</p>"

@app.route("/probe")
def probe():
    return "<p>welcome to the probe!</p>"

@app.route("/upload")
def upload():
    return "<p>Upload CDR CSV here!</p>"