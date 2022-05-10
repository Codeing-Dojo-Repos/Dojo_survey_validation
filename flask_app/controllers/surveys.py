from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_form():
    print(request.form)
    if not Survey.validate_survey(request.form):
        return redirect('/')
    session.clear()
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def handle_result():
    return render_template('result.html')