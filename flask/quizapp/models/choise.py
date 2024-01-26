from quizapp import db

class Choise(db.Model):
    __tablename__ = 'choise'
    quiz_id = db.Column(db.String(10), primary_key=True)
    question_no = db.Column(db.String(1), primary_key=True)
    choise_no = db.Column(db.String(1), primary_key=True)
    choise_content = db.Column(db.String(1000))
    correct_flg = db.Column(db.Boolean)
    