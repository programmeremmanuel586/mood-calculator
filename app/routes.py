from app import app
from flask import render_template, redirect, request, url_for
from app.models import model, formopener

score = 0 

@app.route('/')
@app.route('/index')
def index():
    score = 0
    return render_template("index.html")
    
    
# to question 1
@app.route('/question/<number>', methods=["GET","POST"])
def question(number):
    if request.method == "POST":
        global score
        choice = request.form["choice"]
        score = model.get_score(score, choice)
    question_dict = {
        "1": "question_one.html",
        "2": "question_two.html",
        "3": "question_three.html"
    }

    return render_template(question_dict[number])


# to results page
@app.route('/results', methods=["GET", "POST"])
def results():
    if request.method == "POST":
        global score
        choice = request.form["choice"]
        score = model.get_score(score, choice)
        # return str(score)
        return render_template('results.html')
    

@app.route('/back_to_homepage')
def back_to_homepage():
    return redirect('/index')
    
