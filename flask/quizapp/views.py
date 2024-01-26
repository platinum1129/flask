from flask import render_template, request, redirect, url_for
from quizapp import app
from quizapp import db
from quizapp.models.quiz import Quiz
from quizapp.models.question import Question

@app.route('/')
def index():
    my_dict = {
        'insert_something1': 'views.pyのinsert_something1部分です。',
        'insert_something2': 'views.pyのinsert_something2部分です。',
        'test_titles': ['title1', 'title2', 'title3']
    }
    return render_template('pages/index.html', my_dict=my_dict)

@app.route('/add_quiz', methods=['GET', 'POST'])
def add_quiz():
    print("add_quiz start")
    if request.method == 'GET':
        return render_template('pages/add_quiz.html')
    if request.method == 'POST':

        form_theme = request.form.get('theme')
        form_questions = request.form.get('questions')

        quiz = Quiz(
            source_id = '1',
            quiz_id = '1',
            question_count = form_questions,
        )
        db.session.add(quiz)

        question = Question(
            quiz_id = '1',
            question_no = '1',
            question_content = form_theme,
            explanation = '',
            correct_no = '1'
        )
        db.session.add(question)

        db.session.commit()
        return redirect(url_for('index'))