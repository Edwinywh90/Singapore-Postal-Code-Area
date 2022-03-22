# Singapore-Postal-Code-Area

The idea is to grab subzone, area and region of all possible postal code in Singapore by using OneMap and URA API.

# Python Virtual Environment
`python -m venv venv`

## To go into virtual environment

### For macos
`source venv\bin\activate`

### For windows
`.\venv\Scripts\activate`

## Install dependencies
`pip install -r requirements.txt`

### To export dependencies
`pip freeze > requirements.txt`

# Singapore Postal Code
Singapore has 28 districts according to https://www.ura.gov.sg/realEstateIIWeb/resources/misc/list_of_postal_districts.htm

`PostalCode` class is to scrape the table from the website above and retrieve all valid postal code prefixes to avoid unnecessary postal code requests.

# One Map
The OneMap API used here is able to return `latitude` and `longitude` by providing postal code into `searchVal`.

*we are allow to request 250 API per minute.*

# URA
The URA API used here is able to return `subzone`, `area` and `region` by providing `latitude` and `longitude`.

# How it works
simply call `python main.py` in virtual environment.

    (venv) PS C:\Singapore-Postal-Code-Area> python main.py

## Log file
```
2022-03-21 19:46:56 WARNING one_map.py 143009 has no result.
2022-03-21 19:46:56 WARNING one_map.py 143010 has no result.
2022-03-21 19:46:57 WARNING one_map.py 153009 has no result.
2022-03-21 19:46:58 WARNING one_map.py 153010 has no result.
2022-03-21 19:46:58 INFO one_map.py {'postal_code': '163009', 'lat': '1.28681417822795', 'lng': '103.828928312802'}
2022-03-21 19:46:59 INFO ura.py {'postal_code': '163009', 'lat': '1.28681417822795', 'lng': '103.828928312802', 'region': 'Central Region', 'area': 'Bukit Merah', 'subzone': 'Tiong Bahru'}
2022-03-21 19:47:00 INFO one_map.py {'postal_code': '163010', 'lat': '1.28683793317038', 'lng': '103.838674084243'}
2022-03-21 19:47:01 INFO ura.py {'postal_code': '163010', 'lat': '1.28683793317038', 'lng': '103.838674084243', 'region': 'Central Region', 'area': 'Outram', 'subzone': "Pearl'S Hill"}
2022-03-21 19:47:01 WARNING one_map.py 093009 has no result.
2022-03-21 19:47:02 WARNING one_map.py 093010 has no result.
```

## Output file
```
postal_code;lat;lng;region;area;subzone
163009;1.28681417822795;103.828928312802;Central Region;Bukit Merah;Tiong Bahru
163010;1.28683793317038;103.838674084243;Central Region;Outram;Pearl'S Hill
313010;1.33691012993385;103.858049346644;Central Region;Toa Payoh;Pei Chun
333010;1.31584236197018;103.860644539729;Central Region;Kallang;Bendemeer
463010;1.3217708591015;103.936326570445;East Region;Bedok;Bedok South
```
