
from flask import Flask, render_template
from flask import request




app = Flask(__name__)

# app routes

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test/')
def test():
    return render_template("test.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/schedule/')
def schedule():
    return render_template("schedule.html")

@app.route('/login/')
def login():
    return render_template("login/login.html")

# recipes

@app.route('/recipe-temp/')
def recipetemp():
    return render_template("recipes/recipe_base.html")

@app.route('/quiz/')
def quiz():
    return render_template("quiz.html")

@app.route('/faq/')
def faq():
    return render_template("faq.html")

@app.route('/feedback/', methods=['GET', 'POST'])
def feedback():
    if request.form:
        input = request.form.get("feed1")
        name = request.form.get("feed2")
        if len(input) != 0:  # input field has content
            return render_template("feedback.html", input=input, name=name)
    return render_template("feedback.html")

# run code

@app.route('/signup/')
def signup():
    return render_template("signup.html")

@app.route('/poll/')
def poll():
    return render_template("poll.html")

@app.route('/gallery/')
def gallery():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run(debug=True)