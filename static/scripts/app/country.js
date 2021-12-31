$(document).ready(function () {
    var country = document.getElementById('country_id').innerHTML;
    var country_url = '/get_country/' + country;
    function getData(url) {
      return fetch(url)
      .then((response) => { return response.json() });
    }
    getData(country_url).then((data) => {
      datesD = ['date'];
      number_of_countriesD = ['deaths'];
  
      for (const [key, value] of Object.entries(data['deaths'])){
        datesD.push(key);
        number_of_countriesD.push(value);
      }
  
    var chart = c3.generate({
      bindto: '#chart_deaths',
      data: {
        x: 'date',
        columns: [
          datesD,
          number_of_countriesD
        ],
        types: {
          'deaths': 'area',
          'deaths_trend': 'spline',
        },
        colors:{
          'deaths': '#ff0000',
          'deaths_trend': 'darkorange',
        }
      },
      axis: {
        x: {
            type: 'category',
            "tick": {
                "culling": {
                    "max": 24
                },
                "width": 300,
                "rotate": -30
            },
        }
    }
    });
  
    datesC = ['date'];
    number_of_countriesC = ['cases'];
  
    for (const [key, value] of Object.entries(data['cases'])){
      datesC.push(key);
      number_of_countriesC.push(value);
    }
  
    var chart = c3.generate({
      bindto: '#chart',
      data: {
        x: 'date',
        columns: [
          datesC,
          number_of_countriesC
        ],
        types: {
          'cases':'area',
          'cases_trend':'spline'
        },
        colors:{
          'cases': '#0000ff',
          'cases_trend': 'darkorange',
        }
      },
      axis: {
        x: {
            type: 'category',
            "tick": {
                "culling": {
                    "max": 24
                },
                "width": 300,
                "rotate": -30
            },
        }
    }
    });
    });
  });