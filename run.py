from flask import Flask
from datetime import datetime  
import pytz  

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')  
def current_time():
    new_york_tz = pytz.timezone('America/New_York')
    now = datetime.now(new_york_tz)
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")  
    return 'Current time in New York: {}'.format(current_time)


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
