# covid19 reducer
# reduce covid19 country data with filters

class Reducer:
    def count_country(self, cases_records, deaths_records):
        '''
        input: 
            cases_records - [{country-weekly-record}*]
            deaths_records - [{country-weekly-record}*]
        output:
            counts - 
                { 'deaths': number-of-death, 
                  'cases': number-of-cases, 
                  'mortality': number-of-mortality, 
                  'infection': infection-rate, 
                  'population': population, 
                  'week': year-week
                  }
        '''
        counts = {}

        for country, records in cases_records.items():
            counts[country] = {}
            counts[country]['cases'] = 0
            for record in records:
                cases = int(record['weekly_count'])
                counts[country]['cases'] = counts[country]['cases'] + cases
                population = record['population']
                week = record['year_week']
            counts[country]['population'] = population
            counts[country]['infection'] = round(counts[country]['cases'] / population * 100 ,2)
            counts[country]['week'] = week

        for country, records in deaths_records.items():
            counts[country]['deaths'] = 0
            for record in records:
                deaths = int(record['weekly_count'])
                counts[country]['deaths'] = counts[country]['deaths'] + deaths
                population = record['population']
            counts[country]['population'] = population
            if counts[country]['cases']  == 0:
                counts[country]['mortality'] = 0
            else:
                counts[country]['mortality'] = round( counts[country]['deaths'] / counts[country]['cases']  * 100 ,2)

        return counts
        