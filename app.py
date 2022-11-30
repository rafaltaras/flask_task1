from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/greeting')
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return redirect("/innastrona")


@app.route('/innastrona', methods=['GET'])
def innastrona():
    return 'Witam na innej stronie'

@app.route('/klient/<numer>')
def klient(numer):
    return f'Klient o numerze {numer} to ...'

@app.route('/dodaj/<numer1>+<numer2>')
def dodaj(numer1,numer2):
    wynik = int(numer1) + int(numer2)
    return f'Wynik: {wynik}'

@app.route('/message', methods=['POST'])
def message():
    print(request.form)
    return redirect("/greeting")

@app.route("/warehouse_ugly")
def warehouse_ugly():
    items = ["screwdriver", "hammer", "saw"]
    html = "<ul>"
    for item in items:
        html = html + f"<li>{item}</li>"
    html += "</ul>"
    return html

@app.route("/warehouse")
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    return render_template("warehouse.html", items=items, errors = "Errors")

@app.route("/warehouse2")
def warehouse2():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("warehouse2.html", items=items, errors=errors)


if __name__ == '__main__':
    app.run(debug=True)