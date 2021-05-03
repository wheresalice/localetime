from datetime import datetime
from babel.dates import format_time

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def time():
    locale = request.args.get("locale", 'en_GB')
    date_time = datetime.now()
    locale_time = format_time(date_time, locale=locale)
    return f'<h1 style="font-size:13em;text-align:center">{locale_time}</h1>'


if __name__ == '__main__':
    app.run()
