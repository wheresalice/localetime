from datetime import datetime
from babel.dates import format_time

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def time():
    locale = request.args.get("locale", 'en_GB')
    date_time = datetime.now()
    return format_time(date_time, locale=locale)


if __name__ == '__main__':
    app.run()
