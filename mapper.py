# covid19 mapper
# map raw data to country data

class Mapper:
    def __init__(self, data):
        self.data = data

    def moving_average(self, data, n_num):
        """
        Input:
        data - array of integer
        n - integer
        Output:
        last_n_average:
        moving averaage of last n items
        item for first n item
        """

        last_n_average = [data[i] for i in range(n_num)]
        for i in range(n_num, len(data)):
            last_n = [data[i] for i in range(i - n_num, i)]
            average = round(sum(last_n) / n_num)
            last_n_average.append(average)

        return last_n_average

    def map_continent(self, continent = 'all'):
        '''
        input:
            data

                {
                "country" : "United Kingdom",
                "country_code" : "GBR",
                "continent" : "Europe",
                "population" : 68059863,
                "indicator" : "cases",
                "weekly_count" : 0,
                "year_week" : "2020-01",
                "cumulative_count" : 0,
                "source" : "Epidemic intelligence national data"
            }

        output:
            country_combined_cases - [{'{country}': [{country-weekly-case}}*]]
            country_combined_deaths - [{'{country}': [{country-weekly-death}}*]]
        '''

        country_cases = []
        country_deaths = []

        for record in self.data:
            country = record['country']

            if continent in ['Europe', 'Asia', 'America', 'Africa', 'Oceania']:
                if record['continent'] == continent:
                    if record['indicator'] == 'cases':
                        country_cases.append((country,record))
                    if record['indicator'] == 'deaths':
                        country_deaths.append((country, record))
            else:
                if record['indicator'] == 'cases':
                        country_cases.append((country,record))
                if record['indicator'] == 'deaths':
                        country_deaths.append((country, record))
        
        country_combined_cases = {}

        for country, record in country_cases:
                if country not in country_combined_cases.keys():
                    country_combined_cases[country] = [record]
                else:
                    country_combined_cases[country].append(record)

        country_combined_deaths = {}

        for country, record in country_deaths:
                if country not in country_combined_deaths.keys():
                    country_combined_deaths[country] = [record]
                else:
                    country_combined_deaths[country].append(record)

        self.country_cases = country_combined_cases
        self.country_deaths = country_combined_deaths
    
    def fit_country(self, country):
        country_day_deaths = {}
        country_day_cases = {}

        for record in self.country_cases[country]:
            country_day_cases[record['year_week']] = record['weekly_count']
        
        for record in self.country_deaths[country]:
            country_day_deaths[record['year_week']] = record['weekly_count']

        import datetime

        sorted_deaths = {k: v for k, v in sorted(country_day_deaths.items(), key=lambda item: item[0])}
        sorted_cases =  {k: v for k, v in sorted(country_day_cases.items(), key=lambda item: item[0])}

        from numpy import polyfit as pf
        x_axis = [x for x in range(len(sorted_deaths.keys()))]
        deaths_axis = [int(y) for y in sorted_deaths.values()]
        cases_axis  = [int(y) for y in sorted_cases.values()]

        deaths_trend =  deaths_axis
        if len(deaths_axis)>7:
            deaths_trend = self.moving_average(deaths_axis, 7)

        cases_trend = cases_axis
        if len(cases_trend) > 7:
            cases_trend = self.moving_average(cases_axis,7)

        x_last7 = [x for x in range(7)]
        last_7_week_deaths =  deaths_axis[-7:]
        last_7_week_cases =  cases_axis[-7:]
        
        if len(last_7_week_cases) == 7 and len(last_7_week_deaths) == 7:
            fitted_last7_deaths = pf(x_last7, last_7_week_deaths, 1)
            fitted_last7_cases = pf(x_last7, last_7_week_cases, 1)
        else:
            fitted_last7_deaths = [0,0]
            fitted_last7_cases = [0,0]


        result = {}
        result['deaths'] = sorted_deaths
        result['totaldeaths'] = sum(deaths_axis)
        result['cases']  = sorted_cases
        result['totalcases'] = sum(cases_axis)
        result['deaths_trend'] = deaths_trend
        result['cases_trend'] = cases_trend
        result['death_grow'] = round(fitted_last7_deaths[0],0)
        result['case_grow'] = round(fitted_last7_cases[0],0)
        result['last7deaths'] = last_7_week_deaths
        result['last7cases'] = last_7_week_cases
    
        return result
