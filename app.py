from flask import Flask

app = Flask(__name__)

# routing
@app.route('/') #index
def halo():
    return "Halo duniamu"
