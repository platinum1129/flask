from flask import Flask

app = Flask(__name__)
app.config.from_object('quizapp.config')

import quizapp.views
