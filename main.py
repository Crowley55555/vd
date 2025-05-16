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

from flask import Flask, render_template
from datetime import datetime
import pytz
from tzlocal import get_localzone

app = Flask(__name__)

def get_current_datetime():
    local_tz = get_localzone()  # Получаем часовой пояс пользователя
    now = datetime.now(local_tz)
    return {
        'date': now.strftime('%d.%m.%Y'),
        'time': now.strftime('%H:%M:%S'),
        'timezone': str(local_tz)
    }

@app.route('/')
def start_page():
    return render_template("index.html", datetime=get_current_datetime())

@app.route('/blog/')
def blog_page():
    return render_template("blog.html", datetime=get_current_datetime())

@app.route('/contacts/')  # Исправлено: был дублирующийся route '/'
def contacts_page():
    return render_template("contacts.html", datetime=get_current_datetime())

if __name__ == '__main__':
    app.run()