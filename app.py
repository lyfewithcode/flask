from flask import Flask, render_template

app = Flask(__name__)

# routing
@app.route('/') #index
def home():
    # return "Halo duniamu"
    return render_template('index.html')

@app.route('/profil')
def profil():
    return render_template('profil.html')
