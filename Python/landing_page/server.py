from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')

def index():
    #return "this is working"
    return render_template('index1.html')

@app.route('/ninjas')
def ninjas():
    #print "maybe working"
    return render_template('/ninjas.html')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

app.run(debug=True, port=8888)
