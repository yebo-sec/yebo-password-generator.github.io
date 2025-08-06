from flask import Flask, render_template, request  # type: ignore
import random

app = Flask(__name__)


def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    random.seed()
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        password = generate_password(length)
        return render_template('index.html', password=password)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
# Python Intesivo - Password Generator
