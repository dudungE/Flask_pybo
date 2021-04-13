# 헷갈리니 분류해서 별도로 정리

from flask import Blueprint, render_template, request, url_for, g
from werkzeug.utils import redirect
from Pybo.models import Question, Answer
from datetime import datetime
from Pybo import db
from ..forms import QuestionForm, AnswerForm
from Pybo.views.auth_views import login_required

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def qlist():
    page = request.args.get('page', type=int,default=1)
    question_lst = Question.query.order_by(Question.create_date.desc())
    question_lst = question_lst.paginate(page, per_page=10)

    print(question_lst.total)
    print(question_lst.per_page)

    return render_template('question/question_list.html', question_list=question_lst)



@bp.route('/detail/<int:question_id>/')       #<>는 변수취급함을 의미하는 tag
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/' , methods=('GET', 'POST'))

@login_required

def create():
    form = QuestionForm()


    if request.method == "POST" and form.validate_on_submit():
        q = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now(),user=g.user)
        db.session.add(q)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('question/question_form.html', form=form)
