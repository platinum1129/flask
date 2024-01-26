from quizapp import db

class Question(db.Model):
    __tablename__ = 'question'
    quiz_id = db.Column(db.String(10), primary_key=True)
    question_no = db.Column(db.String(1), primary_key=True)
    question_content = db.Column(db.String(1000))
    explanation = db.Column(db.String(1000))
    correct_no = db.Column(db.String(1))
    