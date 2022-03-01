from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return render_template("base.html", title="Главная")


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('reg_form.html', title='Регистрация')
    elif request.method == 'POST':
        param = {}
        param['email'] = request.form['email']
        param['password'] = request.form['pass']
        param['check'] = request.form['check']
        return render_template('success.html', data=param)


@app.route("/success")
def success():
    return render_template("success.html", title="Успешно")
    

def main():
    app.run(port=5005)


if __name__ == '__main__':
    main()
