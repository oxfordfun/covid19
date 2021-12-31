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

    mapper = Mapper(data)
    if len(sys.argv) > 2:
        query_continent = sys.argv[2]
        mapper.map_continent(query_continent)
    else:
         mapper.map_continent()
    
    # get stats of each country
    reducer = Reducer(mapper.country_cases, mapper.country_deaths)
    reducer.count_country()
    
    output_json = json.dumps(reducer.counts, indent=4)
    print(output_json)

    output = mapper.fit_country('United Kingdom')
    print(output)
    