from quizapp import db

class Quiz(db.Model):
    __tablename__ = 'quiz'
    source_id = db.Column(db.String(10))
    quiz_id = db.Column(db.String(10), primary_key=True)
    question_count = db.Column(db.Integer)
    