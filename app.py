from flask import Flask, request, render_template
from surveys import satisfaction_survey

app = Flask(__name__)

responses = []


@app.route('/')
def render_home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)


@app.route('/questions/0')
def render_firstQ():
    index = satisfaction_survey.questions.index(
        satisfaction_survey.questions[0]) + 1
    firstQ = satisfaction_survey.questions[0].question
    choiceOne = satisfaction_survey.questions[0].choices[0]
    choiceTwo = satisfaction_survey.questions[0].choices[1]
    return render_template('questions.html', firstQ=firstQ, choiceOne=choiceOne, choiceTwo=choiceTwo, index=index)


@app.route('/questions/1')
def render_secondQ():
    index = satisfaction_survey.questions.index(
        satisfaction_survey.questions[1]) + 1
    firstQ = satisfaction_survey.questions[1].question
    choiceOne = satisfaction_survey.questions[1].choices[0]
    choiceTwo = satisfaction_survey.questions[1].choices[1]
    return render_template('questions.html', firstQ=firstQ, choiceOne=choiceOne, choiceTwo=choiceTwo, index=index)


@app.route('/questions/2')
def render_thirdQ():
    index = satisfaction_survey.questions.index(
        satisfaction_survey.questions[2]) + 1
    firstQ = satisfaction_survey.questions[2].question
    choiceOne = satisfaction_survey.questions[2].choices[0]
    choiceTwo = satisfaction_survey.questions[2].choices[1]
    return render_template('questions.html', firstQ=firstQ, choiceOne=choiceOne, choiceTwo=choiceTwo, index=index)


@app.route('/questions/3')
def render_fourthQ():
    index = satisfaction_survey.questions.index(
        satisfaction_survey.questions[3]) + 1
    firstQ = satisfaction_survey.questions[3].question
    choiceOne = satisfaction_survey.questions[3].choices[0]
    choiceTwo = satisfaction_survey.questions[3].choices[1]
    return render_template('questions.html', firstQ=firstQ, choiceOne=choiceOne, choiceTwo=choiceTwo, index=index)


@app.route('/questions/4')
def render_thanks():
    return render_template('thanks.html')
