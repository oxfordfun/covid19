$(document).ready(function () {
    var country = document.getElementById('country_id').innerHTML;
    var country_url = '/get_country/' + country;
    function getData(url) {
      return fetch(url)
      .then((response) => { return response.json() });
    }
    getData(country_url).then((data) => {
      datesD = ['date'];
      number_of_countriesD = ['weekly_deaths'];
  
      for (const [key, value] of Object.entries(data['deaths'])){
        datesD.push(key);
        number_of_countriesD.push(value);
      }

      dots_deaths = ['last4weeks_average'] 

      for (const [key, value] of Object.entries(data['deaths_trend'])){
        dots_deaths.push(value);
      }
  
    var chart = c3.generate({
      bindto: '#chart_deaths',
      data: {
        x: 'date',
        columns: [
          datesD,
          number_of_countriesD,
          dots_deaths
        ],
        types: {
          'weekly_deaths': 'area',
          'deaths_trend': 'spline',
        },
        colors:{
          'weekly_deaths': '#ff0000',
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
    number_of_countriesC = ['weekly_cases'];
  
    for (const [key, value] of Object.entries(data['cases'])){
      datesC.push(key);
      number_of_countriesC.push(value);
    }

    dots_cases = ['last4weeks_average'] 

    for (const [key, value] of Object.entries(data['cases_trend'])){
       dots_cases.push(value);
    }
  
    var chart = c3.generate({
      bindto: '#chart',
      data: {
        x: 'date',
        columns: [
          datesC,
          number_of_countriesC,
          dots_cases
        ],
        types: {
          'weekly_cases':'area',
          'cases_trend':'spline'
        },
        colors:{
          'weekly_cases': '#0000ff',
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