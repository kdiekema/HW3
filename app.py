from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle = 'My Loan Calculator')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        form = request.form
        a = float(form['a'])
        n = float(form['n'])
        i = float(form['i'])
        d = (((1+i)**n)-1)/(((1+i)**n)*i)
        calculate = '${:,.2f}'.format(a/(d))
        return render_template('index.html', display=calculate, pageTitle="My Loan Calculator")

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
