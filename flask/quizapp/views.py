from flask import render_template, request, redirect, url_for
from quizapp import app
from quizapp import db
from quizapp.models.quiz import Quiz
from quizapp.models.question import Question
from quizapp.models.choice import Choice
import os
import openai
import json

openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/add_quiz', methods=['GET', 'POST'])
def add_quiz():

    print("ChatGPT Start")

    form_theme = request.form.get('theme')
    form_questions = request.form.get('questions')

    req_content = '「' + form_theme + '」に関する4択クイズを作成して。'\
                + '・問題数：' + form_questions + '問'\
                + '・正答率の目標：50% 普通程度に'\
                + '・レスポンスはJSON形式'\
                + '・作成できない場合、{"error":""}を返す'\
                + '・選択肢は1～4のランダムになるようにしてください'\
                + '・コードスニペットは不要'\
                + 'レスポンス例：'\
+ '''
[
  {
    "question": "太陽系で最も大きな天体はどれ？",
    "choices": [
      "地球",
      "太陽",
      "月",
      "火星"
    ],
    "correct": "2"
  },
  {
    "question": "宇宙空間にはどのくらいの星が存在すると考えられている？",
    "choices": [
      "100億個",
      "1000億個",
      "100兆個",
      "無限個"
    ],
    "correct": "3"
  }
]
'''
    res_content_question = callChatGPT(req_content)

    print("add_quiz start")
    if request.method == 'GET':
        return render_template('pages/index.html')

    if request.method == 'POST':

        db.session.query(Quiz).delete()
        db.session.query(Question).delete()
        db.session.query(Choice).delete()

        res_dict = json.loads(res_content_question)

        print(res_dict)

        form_source_id = '0'
        form_quiz_id = '1'

        quiz = Quiz(
            source_id = form_source_id,
            quiz_id = form_quiz_id,
            question_count = form_questions,
        )
        db.session.add(quiz)

        for i in range(len(res_dict)):

            res_question = res_dict[i - 1]['question']
            res_correct = res_dict[i - 1]['correct']
            res_choices = res_dict[i - 1]['choices']
            res_explanation = ''
            # res_explanation = callChatGPT(
            #      res_question + 'に対する答えと解説を200文字以内で作成して'
            # )

            question = Question(
                quiz_id = form_quiz_id,
                question_no = i,
                question_content = res_question,
                explanation = res_explanation,
                correct_no = res_correct
            )
            db.session.add(question)

            choice_no = 0
            for res_choice in res_choices:
                choice_no += 1
                choice = Choice(
                    quiz_id = form_quiz_id,
                    question_no = i,
                    choice_no = choice_no,
                    choice_content = res_choice,
                    correct_flg = False
                )
                db.session.add(choice)

        db.session.commit()
        return redirect(url_for('index'))
    

def callChatGPT(req_content):
    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    # model="gpt-4-turbo-preview",
    temperature=1.0,
    messages=[{
            "role": "user",
            "content": req_content
    }],
    )
    print(response)
    print("###############################################################################")
    print(response.choices[0].message.content)
    print("ChatGPT End")
    return response.choices[0].message.content.strip("```json")
