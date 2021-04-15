from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
from sqlalchemy import MetaData

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(config)
app.debug = True

    #ORM 데이터베이스 초기화
db.init_app(app)

if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
    migrate.init_app(app, db, render_as_batch=True)
else:
    migrate.init_app(app, db)


from .views import main_views, question_views, answer_views, auth_views, chatbotviews
app.register_blueprint(main_views.bp)
app.register_blueprint(question_views.bp)
app.register_blueprint(answer_views.bp)
app.register_blueprint(auth_views.bp)

app.register_blueprint(chatbotviews.bp)



#필터등록
from .filter import format_datetime
app.jinja_env.filters['datetime'] = format_datetime




from . import models
from Pybo.models import Question,Answer
from datetime import datetime

@app.route('/question')
def Insert_question():
    q = Question(subject='이것은 무엇인가요?', content='알려주세요 궁금합니다.',create_date=datetime.now())
    q.subject='[질문]이것은 무엇일까요?'
    db.session.add(q)
    db.session.commit()
    return 'Sucess'

@app.route('/question_all')
def Get_question():

    '''
    q =     Question.query.all()   #모든데이터 조회
    print('------id : ',q[1].id)
    print('------subject : ', q[1].subject)
    print('------content : ', q[1].content)

    return 'Sucess'
    '''

    '''
    q = Question.query.get(4)  #pk 가 1번인 데이터를 가져온다.
    print('------id : ', q.id)
    print('------subject : ', q.subject)
    print('------content : ', q.content)
    return 'Sucess'
    '''


    '''
    q = Question.query.filter(Question.subject.ilike('%무엇%')).all()   #제목에서 무엇이 들어간 제목을 가져온다.
    print(q)
    return 'Sucess'

    '''


    '''
    q = Question.query.get(3) #데이터의 내용을 수정
    q.subject = '질문내용1'
    db.session.commit()
    return 'Sucess'
    '''


    '''
    q = Question.query.get(2) #데이터 삭제
    db.session.delete(q)
    db.session.commit()
    return 'Success'
    '''


    '''
    q = Question.query.get(2) #답변 및 참조 가져오는 방법
    a = Answer(question=q , content='답변 생성입니다.',create_date=datetime.now())
    db.session.add(a)
    db.session.commit()
    return 'Success'
    '''

    '''
    a = Answer.query.get(1)
    q = a.question
    qall = q.answer_set
    print(qall)
    '''




