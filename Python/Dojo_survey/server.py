from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'mySecretKey'
@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/result', methods=['POST'])
def dojo_info():
    session['name'] = request.form['name']
    print (session['name'])
    session['location'] = request.form['location']
    print (session['location'])
    session['language'] = request.form['language']
    print (session['language'])
    session['comment'] = request.form['comment']
    print (session['comment'])

    return redirect('/submit')

@app.route('/submit')
def results():
    return render_template('result.html')

app.run(debug=True, port=9999)
