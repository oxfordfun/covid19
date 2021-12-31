import json

from flask import Flask, render_template, abort, request, redirect
from flask import flash, url_for, make_response

from mapper import Mapper
from reducer import Reducer

app = Flask(__name__)

@app.route("/countries")
def get_countries():
    return render_template(
        "countries.template", counts = reducer.counts
    )

@app.route("/get_country/<country>")
def proxy_get_country(country):
    data = mapper.fit_country(country)
    return json.dumps(data)

@app.route("/country/<country>")
def get_country(country):
    cases = mapper.country_cases[country]
    deaths = mapper.country_deaths[country]
    return render_template(
        "country.template", cases = cases, deaths = deaths, country = country
    )

if __name__ == "__main__":
    global data, mapper, reducer
    with open('data.json') as reader:
        data = json.loads(reader.read())
    mapper = Mapper(data)
    mapper.map_continent()
    # get stats of each country
    reducer = Reducer(mapper.country_cases, mapper.country_deaths)
    reducer.count_country()

    app.run(host="127.0.0.1", port=6060)