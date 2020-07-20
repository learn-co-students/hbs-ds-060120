from datetime import datetime
import json

from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def asdfasdf():
    return """
<html>
<head>
<title>Andy's awesome website</title>
</head>
<body>
<h1>Hello, World!</h1>
The current time is {}

<a href="{}">Link to goodbye</a>
</body>
</html>
""".format(datetime.now().strftime('%H:%M:%S'),
           url_for('goodbye_world'))

@app.route('/current_time')
def hello_world():
    return json.dumps({'current_datetime': datetime.now().isoformat()})

@app.route('/goodbye')
def goodbye_world():
    return """
    <html>
    <head>Andy's cool site</head>
    <body>
    <h1><div style="color:red">goodbye, World =(</div></h1>
    </body>
    </html>
    """

# @app.route('/ss')
# def space_station():
# 	r = requests.get('http://api.open-notify.org/iss-now.json')
# 	return r.content
