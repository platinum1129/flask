from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('quizapp.config')

db = SQLAlchemy(app)
from .models import quiz
from .models import question
from .models import choise

import quizapp.views
