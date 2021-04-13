from flask import Blueprint, render_template, url_for
from Pybo.models import Question, Answer
from datetime import datetime
from Pybo import db
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


# @bp.route('/')
# def hello_pybo():
#     q = Question(subject='이것은 무엇인가요?', content='알려주세요 궁금합니다.', create_date=datetime.now())
#     q.subject = '[질문]이것은 무엇일까요?'
#     db.session.add(q)
#     db.session.commit()
#     return 'success'


@bp.route('/')
def index():
    return redirect(url_for('question.qlist'))  # question 이라는 블루프린트에 qlist함수로 주소를 넘겨라


@bp.route('/test')
def test():
    for i in range(300):
        q = Question(subject='테스트 데이터입니다. {0}'.format(i), content='내용무', create_date=datetime.now())
        db.session.add(q)
    db.session.commit()
    return 'success'




