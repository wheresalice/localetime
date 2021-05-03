from datetime import datetime
from babel.dates import format_time, format_date

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def time():
    locale = request.args.get("locale", 'en_GB')
    date_time = datetime.now()
    locale_time = format_time(date_time, format='short', locale=locale)
    locale_date = format_date(date_time, locale=locale)
    return f'<div><h1 style="font-size:13em;text-align:center">{locale_time}</h1></div><div><h1 style="font-size:13em;text-align:center">{locale_date}</h1></div>'


if __name__ == '__main__':
    app.run()
