import json

from flask import Flask, render_template, abort, request, redirect
from flask import flash, url_for, make_response

from mapper import Mapper
from reducer import Reducer

app = Flask(__name__)

@app.route("/countries")

def get_country():
    return render_template(
        "countries.template", counts = reducer.counts
    )

if __name__ == "__main__":
    global data, mapper, reducer
    with open('data/2021-51.json') as reader:
        data = json.loads(reader.read())
    mapper = Mapper(data)
    mapper.map_continent()
    # get stats of each country
    reducer = Reducer(mapper.country_cases, mapper.country_deaths)
    reducer.count_country()

    app.run(host="127.0.0.1", port=3322)