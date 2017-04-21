from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')

def hello():
    name = "Robert"
    age = 10
    return render_template('index.html', name=name, age=age)


@app.route('/numbers')
def numbers():
    for number in range(3):
        print "we're in number"
    return redirect('/')

@app.route('/second')
def second():
    print "you got to the second page"
    return render_template('second.html')

app.run(debug=True, port=8888)
