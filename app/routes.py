from app import app
from flask import render_template, redirect, request, url_for, session
from app.models import model, formopener

app.secret_key = b'=\xcf\xe8\x85o\xb54W\xf9\xf0\x9dz$\xa2\x8f^\xd9\x0e\xc2\xdc\x95ON.\x85\xe4\xf9\xc6\x8c\xed\xf7V'




@app.route('/')
@app.route('/index')
def index():

    session['score'] = 0
    return render_template("index.html")
    
    
# to question 1
@app.route('/question/<number>', methods=["GET","POST"])
def question(number):
    if request.method == "POST":
        choice = request.form["choice"]
        session['score'] = model.get_score(session['score'], choice)
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
        choice = request.form["choice"]
        session['score'] = model.get_score(session['score'], choice)
        mood = model.get_mood(session['score'])
        print(mood)
        # return str(score)
        if mood == "Happy":
            return render_template('/results_Happy.html')
        elif mood == "Sad":
            return render_template('/results_Sad.html')
        elif mood == "Meh":
            return render_template('/results_Meh.html')
        else:
            session['score'] = 0
            return redirect('/')   
    else:
        return redirect('/')
    
    

@app.route('/back_to_homepage')
def back_to_homepage():
    session['score'] = 0
    session.clear()
    return redirect('/index')
    
