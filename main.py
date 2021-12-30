import sys
import json

from mapper import Mapper
from reducer import Reducer

if __name__ == "__main__":
    if sys.argv[1]:
        input_file = sys.argv[1]
    else:
        print("data file needed")
        exit()

    with open(input_file) as reader:
        data = json.loads(reader.read())
    
    # mapped to country

    mapper = Mapper()
    if sys.argv[2]:
        query_continent = sys.argv[2]
        country_cases, country_deaths = mapper.map_continent(data, query_continent)
    
    # get stats of each country
    reducer = Reducer()
    country_stats = reducer.count_country(country_cases, country_deaths)

    output_json = json.dumps(country_stats, indent=4)

    print(output_json)
    