from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv(verbose=True)

app = Flask(__name__)
app.config.from_object('quizapp.config')

db = SQLAlchemy(app)
from .models import quiz
from .models import question
from .models import choice

import quizapp.views
