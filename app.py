from datetime import datetime
from babel.dates import format_time, format_date

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def default():
    locale = request.args.get("locale", 'en_GB')
    date_time = datetime.now()
    locale_time = format_time(date_time, locale=locale)
    locale_date = format_date(date_time, locale=locale)
    return f'<div style="display: flex;align-items:center;justify-content:center;"><h1 style="font-size:13em;text-align:center">{locale_time}<br>{locale_date}</h1></div>'


@app.route('/short', methods=['GET'])
def short():
    locale = request.args.get("locale", 'en_GB')
    date_time = datetime.now()
    locale_time = format_time(date_time, format='short', locale=locale)
    locale_date = format_date(date_time, format='short', locale=locale)
    return f'<div style="display: flex;align-items:center;justify-content:center;"><h1 style="font-size:13em;text-align:center">{locale_time}<br>{locale_date}</h1></div>'


@app.route('/long', methods=['GET'])
def long():
    locale = request.args.get("locale", 'en_GB')
    date_time = datetime.now()
    locale_time = format_time(date_time, format='long', locale=locale)
    locale_date = format_date(date_time, format='long', locale=locale)
    return f'<div style="display: flex;align-items:center;justify-content:center;"><h1 style="font-size:13em;text-align:center">{locale_time}<br>{locale_date}</h1></div>'


if __name__ == '__main__':
    app.run()
