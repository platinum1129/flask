from quizapp import db

class Choice(db.Model):
    __tablename__ = 'choice'
    quiz_id = db.Column(db.String(10), primary_key=True)
    question_no = db.Column(db.String(1), primary_key=True)
    choice_no = db.Column(db.String(1), primary_key=True)
    choice_content = db.Column(db.String(1000))
    correct_flg = db.Column(db.Boolean)
    