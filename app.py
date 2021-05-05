from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

RESPONSES_KEY = "responses"
app = Flask(__name__)
app.config["SECRET_KEY"] = "test123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def render_home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)


@app.route('/start', methods=["POST"])
def start_survey():
    session[RESPONSES_KEY] = []
    return redirect("/questions/0")


@app.route('/answers', methods=["POST"])
def render_answers():
    choices = request.form["choices"]
    responses = session[RESPONSES_KEY]
    responses.append(choices)
    session[RESPONSES_KEY] = responses

    if len(responses) == len(satisfaction_survey.questions):
        return redirect("/thanks")
    else:
        return redirect(f"/questions/{len(responses)}")


@app.route('/questions/0')
def render_firstQ():
    responses = session.get(RESPONSES_KEY)
    if (responses is None):
        return redirect("/")

    if (len(responses) == len(satisfaction_survey.questions)):
        return redirect("/thanks")

    if (len(responses) != 0):
        flash("Don't skip ahead! :)")
        return redirect(f"/questions/{len(responses)}")

    firstQ = satisfaction_survey.questions[0].question
    choiceOne = satisfaction_survey.questions[0].choices[0]
    choiceTwo = satisfaction_survey.questions[0].choices[1]
    return render_template('questions.html', firstQ=firstQ, choiceOne=choiceOne, choiceTwo=choiceTwo)


@app.route('/questions/1')
def render_secondQ():
    responses = session.get(RESPONSES_KEY)
    if (responses is None):
        return redirect("/")

    if (len(responses) == len(satisfaction_survey.questions)):
        return redirect("/thanks")

    if (len(responses) != 1):
        flash("Don't skip ahead! :)")
        return redirect(f"/questions/{len(responses)}")

    firstQ = satisfaction_survey.questions[1].question
    choiceOne = satisfaction_survey.questions[1].choices[0]
    choiceTwo = satisfaction_survey.questions[1].choices[1]
    return render_template('questions.html', firstQ=firstQ, choiceOne=choiceOne, choiceTwo=choiceTwo)


@app.route('/questions/2')
def render_thirdQ():
    responses = session.get(RESPONSES_KEY)
    if (responses is None):
        return redirect("/")

    if (len(responses) == len(satisfaction_survey.questions)):
        return redirect("/thanks")

    if (len(responses) != 2):
        flash("Don't skip ahead! :)")
        return redirect(f"/questions/{len(responses)}")

    firstQ = satisfaction_survey.questions[2].question
    choiceOne = satisfaction_survey.questions[2].choices[0]
    choiceTwo = satisfaction_survey.questions[2].choices[1]
    return render_template('questions.html', firstQ=firstQ, choiceOne=choiceOne, choiceTwo=choiceTwo)


@app.route('/questions/3')
def render_fourthQ():
    responses = session.get(RESPONSES_KEY)
    if (responses is None):
        return redirect("/")

    if (len(responses) == len(satisfaction_survey.questions)):
        return redirect("/thanks")

    if (len(responses) != 3):
        flash("Don't skip ahead! :)")
        return redirect(f"/questions/{len(responses)}")

    firstQ = satisfaction_survey.questions[3].question
    choiceOne = satisfaction_survey.questions[3].choices[0]
    choiceTwo = satisfaction_survey.questions[3].choices[1]
    return render_template('questions.html', firstQ=firstQ, choiceOne=choiceOne, choiceTwo=choiceTwo)


@app.route('/thanks')
def render_thanks():
    return render_template('thanks.html')
