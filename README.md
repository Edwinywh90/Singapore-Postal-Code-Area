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
One of the OneMap API is able to return latitude and longitude by providing postal code into `searchVal`.

*we are allow to request 250 APIs per minute.*

# URA
One of the URA API is able to return subzone, area and region by providing latitude and longitude.

# How it works
simply call `python main.py` in virtual environment.

    (venv) PS C:\Singapore-Postal-Code-Area> python main.py
