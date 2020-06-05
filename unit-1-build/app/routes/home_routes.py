# web_app/routes/home_routes.py

from flask import Blueprint, render_template, redirect

from web_app.utils import openaq
from web_app.models import Record, db

home_routes = Blueprint("home_routes", __name__)


@home_routes.route('/')
def root():
    try:
        out = Record.query.filter(Record.value >= 10).all()
    except:
        out = None
    return render_template('index.html', data=out)


@home_routes.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    db.drop_all()
    db.create_all()
    # todo get all of the data from api and save it to a db

    # fetch data
    api = openaq.OpenAQ()
    _, body = api.measurements(city='Los Angeles', parameter='pm25')
    t = body['results']

    # save to list of tuples
    out = []
    for i in t:
        out.append((i['date']['utc'], i['value']))

    # put that list of tuples in a db
    # oneliners mean for each entry in dates and for each entry in values do:
    for k, v in zip([x['date']['utc'] for x in t], [x['value'] for x in t]):
        r = Record()
        r.utc_time = k
        r.value = v
        db.session.add(r)
    db.session.commit()

    return redirect('/')
