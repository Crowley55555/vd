from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
# @app.route('/<password>/')
# def hello(password=None):
#     if password == '1234':
#         return f"Доступ разрешен"
#     else:
#         return f"Доступ запрещен"

def hello():
    return render_template("vd_03.html")

if __name__ == '__main__':
    app.run()

