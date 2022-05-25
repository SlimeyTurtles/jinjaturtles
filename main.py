from flask import render_template, Flask

app = Flask(__name__)

# app routes

@app.route('/')
def index():
    return render_template("index.html")

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

@app.route('/faq/')
def faq():
    return render_template("faq.html")

@app.route('/feedback/')
def feedback():
    return render_template("feedback.html")

# run code

@app.route('/signup/')
def signup():
    return render_template("signup.html")

@app.route('/poll/')
def poll():
    return render_template("poll.html")

if __name__ == "__main__":
    app.run(debug=True)