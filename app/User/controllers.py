from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    abort,
    redirect,
    url_for,
    current_app,
)
from sqlalchemy.exc import SQLAlchemyError


from .models import Users, db
from .forms import RegistrationForm, LoginForm

module = Blueprint('', __name__, url_prefix ='/')


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)


@module.route('/', methods=['GET'])
def index():   
    return render_template('index.html')

@module.route('sign_up', methods=['GET', 'POST'])
def sign_up():   
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            if request.method == 'POST' and form.validate():
                user = Users.query.filter_by(email=form.email.data).first()                
                if user == None:
                    user = Users(form.email.data, form.password.data)
                    db.session.add(user)
                    db.session.flush()
                    id = user.id
                    db.session.commit()
                    flash('Регистрация прошла успешно!', 'success')
                    #return redirect(url_for('entity.view', id=id))
                else:
                    flash('Почта уже есть в базе!', 'success')
        except SQLAlchemyError as e:
            log_error('There was error while querying database', exc_info=e)
            db.session.rollback()
            flash('Произошла непредвиденная ошибка во время запроса к базе данных', 'danger')        
    return render_template('user/sign_up.html', form=form)

@module.route('sign_in', methods=['GET', 'POST'])
def sign_in():   
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            if request.method == 'POST' and form.validate():                
                user = Users.query.filter_by(email=form.email.data).first()                
                if user != None and Users.check_password(form.password.data):
                    
                    flash('Вы успешно авторизовались!', 'success')
                    #return redirect(url_for('entity.view', id=id))
                else:
                    flash('Не верные данные или пользователя не существует', 'success')
        except SQLAlchemyError as e:
            log_error('There was error while querying database', exc_info=e)
            db.session.rollback()
            flash('Произошла непредвиденная ошибка во время запроса к базе данных', 'danger')        
    return render_template('user/sign_in.html', form=form)
