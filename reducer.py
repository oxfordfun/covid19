# covid19 reducer
# reduce covid19 country data with filters


class Reducer:
    def __init__(self, cases_records, deaths_records):
        self.cases_records = cases_records
        self.deaths_records = deaths_records

    def count_country(self):
        """
        input:
            cases_records - [{country-weekly-record}*]
            deaths_records - [{country-weekly-record}*]
        output:
            counts -
                { 'continent': continent,
                  'deaths': number-of-death,
                  'cases': number-of-cases,
                  'mortality': number-of-mortality,
                  'infection': infection-rate,
                  'population': population,
                  'week': year-week,
                  }
        """
        counts = {}

        for country, records in self.cases_records.items():
            counts[country] = {}
            counts[country]["cases"] = 0
            for record in records:
                if "weekly_count" in record.keys():
                    cases = int(record["weekly_count"])
                else:
                    cases = 0
                counts[country]["cases"] = counts[country]["cases"] + cases
                population = record["population"]
                week = record["year_week"]
                continent = record["continent"]
            counts[country]["population"] = population
            counts[country]["infection"] = round(
                counts[country]["cases"] / population * 100, 2
            )
            counts[country]["week"] = week
            counts[country]["continent"] = continent

        for country, records in self.deaths_records.items():
            counts[country]["deaths"] = 0
            for record in records:
                if "weekly_count" in record.keys():
                    deaths = int(record["weekly_count"])
                else:
                    deaths = 0
                counts[country]["deaths"] = counts[country]["deaths"] + deaths
                population = record["population"]
            counts[country]["population"] = population
            if counts[country]["cases"] == 0:
                counts[country]["mortality"] = 0
            else:
                counts[country]["mortality"] = round(
                    counts[country]["deaths"] / counts[country]["cases"] * 100, 2
                )

        self.counts = counts
