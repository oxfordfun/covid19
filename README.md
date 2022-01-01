# Covid19
Show covid19 data, for example:  https://covid19.oxfordfun.com/countries

# Set up

## Clone the code
```
git clone https://github.com/oxfordfun/covid19 
```
## Get data from ECDC
```
wget https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/json -O data.json
```

## Install dependencies in a virtual environment
```
virtualenv -p python3 env
source env/bin/activate
pip3 install -r requirements.txt
```
# Run it
## Command
Show World data

```
python3 main.py data.json > data/world.json 
```

Show Continent data (Europe, Asia, America, Africa, Oceania)

```
python3 main.py data.json Europe > data/europe.json
```

## Web
```
python3 webmain.py data.json 
```
Data shown at http://127.0.0.1:6060/countries

![Countries Data](data/Countries.png?raw=true "Countries")

Data shown at http://127.0.0.1:6060/country/United%20Kingdom

![UK Data](data/Countries.png?raw=true "UK")
