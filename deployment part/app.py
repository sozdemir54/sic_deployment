from flask import Flask, render_template, request
import python_code

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def hello():
    if request.method == "POST":
        hrs =request.form['hrs']
        marks_pred = python_code.prediction(hrs)
        print(marks_pred)
    return render_template("index.html")

@app.route("/sub", methods = ["POST"])
def submit():
    # HTML -> .py
    if request.method == "POST":
        name = request.form["username"]
    
    # .py -> HTML
    return render_template("sub.html", n = name)

if __name__ == "__main__":
    app.run(debug=True)
