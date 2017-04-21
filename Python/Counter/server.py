from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'this is a secret'
@app.route('/')
def index():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 0
    print 'counter is {}'.format(session['counter'])

    return render_template('index.html')

@app.route('/addtwo', methods=['POST'])
def addtwo():
    session['counter'] += 1
    print 'counter is now {}'.format(session['counter'])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('counter')
    print 'counter has been reset'
    return redirect('/')

app.run(debug=True, port=5000)
