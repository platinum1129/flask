from flask import render_template, request, redirect, url_for
from quizapp import app
from quizapp import db
from quizapp.models.quiz import Quiz
from quizapp.models.question import Question
from quizapp.models.choice import Choice
from sqlalchemy import func
import os
import openai
import json

openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/add_quiz', methods=['POST'])
def add_quiz():
    print("add_quiz Start")

    print("ChatGPT Start")

    form_theme = request.form.get('theme')
    form_questions = request.form.get('questions_count')
    form_explain = request.form.get('explain')

    # 生成済問題の取得
    created_questions = set()
    for q in Question.query.all():
        created_questions.add(q.question_content)
    print(created_questions)

    req_content = '「' + form_theme + '」に関する4択クイズを作成して。'\
                + '・問題数：' + form_questions + '問'\
                + '・正答率の目標：50% 普通程度に'\
                + '・レスポンスはJSON形式'\
                + '・作成できない場合、{"error":""}を返す'\
                + '・次の問題は除く：' + str(type(created_questions))\
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
    print('req_content: ' + req_content)
    res_content_question = callChatGPT(req_content)

    db.session.query(Quiz).delete()
    db.session.query(Question).delete()
    db.session.query(Choice).delete()

    res_dict = json.loads(res_content_question)

    print(res_dict)

    # ソースID(0固定)
    form_source_id = '0'

    # クイズID採番
    form_quiz_id = '1'
    # max_quiz_id = db.session.query(func.max(Question.quiz_id)).scalar()
    # if max_quiz_id is None:
    #     max_quiz_id = 1
    # else:
    #     max_quiz_id = int(max_quiz_id) + 1
    # form_quiz_id = str(max_quiz_id)

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
        if form_explain == '1':
            res_explanation = callChatGPT(
                  res_question + 'に対する答えと解説を200文字以内で作成して'
            )

        res_question_no = i + 1
        question = Question(
            quiz_id = form_quiz_id,
            question_no = res_question_no,
            question_content = res_question,
            explanation = res_explanation,
            correct_no = res_correct
        )
        db.session.add(question)

        res_choice_no = 0
        for res_choice in res_choices:
            res_choice_no += 1
            choice = Choice(
                quiz_id = form_quiz_id,
                question_no = res_question_no,
                choice_no = res_choice_no,
                choice_content = res_choice,
                correct_flg = False
            )
            db.session.add(choice)

    db.session.commit()

    # DB登録データ取得
    quizes = Quiz.query.all()
    questions = Question.query.all()
    choices = Choice.query.all()
    print("add_quiz end")
    return render_template('pages/index.html', 
                          theme = form_theme,
                          questions_count = form_questions,
                          explain = form_explain,
                          quizes = quizes,
                          questions = questions,
                          choices = choices
                          )
    

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

