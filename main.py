# from flask import Flask, render_template
# app = Flask(__name__)
#
# @app.route('/')
# def start_page():
#     return render_template("index.html")
#
# @app.route('/blog/')
# def blog_page():
#     return render_template("blog.html")
#
# @app.route('/')
# def contacts_page():
#     return render_template("contacts.html")
#
# if __name__ == '__main__':
#     app.run()

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import pytz
from tzlocal import get_localzone
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Для работы flash-сообщений


def get_current_datetime():
    """Получение текущей даты и времени в часовом поясе пользователя"""
    local_tz = get_localzone()
    now = datetime.now(local_tz)
    return {
        'date': now.strftime('%d.%m.%Y'),
        'time': now.strftime('%H:%M:%S'),
        'timezone': str(local_tz)
    }


@app.route('/')
def start_page():
    """Главная страница"""
    return render_template(
        "index.html",
        datetime=get_current_datetime(),
        active_page='home'
    )


@app.route('/blog/')
def blog_page():
    """Страница блога"""
    # Здесь можно добавить логику для получения постов из базы данных
    return render_template(
        "blog.html",
        datetime=get_current_datetime(),
        active_page='blog'
    )


@app.route('/contacts/', methods=['GET', 'POST'])
def contacts_page():
    """Страница контактов"""
    if request.method == 'POST':
        # Обработка формы обратной связи
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Здесь можно добавить логику для сохранения сообщения в базу данных
        # или отправки email

        flash('Ваше сообщение успешно отправлено!', 'success')
        return redirect(url_for('contacts_page'))

    return render_template(
        "contacts.html",
        datetime=get_current_datetime(),
        active_page='contacts'
    )


@app.errorhandler(404)
def page_not_found(e):
    """Обработка ошибки 404"""
    return render_template(
        "404.html",
        datetime=get_current_datetime()
    ), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Обработка ошибки 500"""
    return render_template(
        "500.html",
        datetime=get_current_datetime()
    ), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)