from flask import Flask,render_template, request
import cyber

app = Flask(__name__)

@app.route('/base', methods = ["POST"])
def submit():
    #html -> python
    if request.method == "POST":
        name = request.form["input_name"]
        final = cyber.make_prediction(name)

    #python -> html
    return render_template("base.html",text = final)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)