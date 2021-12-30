# covid19 mapper
# map raw data to country data

class Mapper:
    def map_continent(self, data, continent = 'all'):
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

        for record in data:
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

        return country_combined_cases, country_combined_deaths
