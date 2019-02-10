from flask import Flask, render_template, request
import profiles

app = Flask(__name__)

@app.route("/index.html")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results.html", methods = ['POST'])
@app.route('/results', methods = ['POST'])
def results():
    Gender = request.form['Gender']
    return render_template("results.html", Gender = g)

@app.route('/ProfileCreation.html')
@app.route('/ProfileCreation')
def ProfileCreation():
    return render_template("ProfileCreation.html")



@app.route("/about.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/ProfileMatch.html")#, methods=['POST'])
@app.route("/ProfileMatch")
def ProfileMatch():
    return render_template("ProfileMatch.html")


if __name__ == "__main__":
    app.run(debug=True)
