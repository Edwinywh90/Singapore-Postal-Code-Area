from ratelimit import limits
from constants import CALLS_PER_MINUTE, MINUTE
import requests
import json
import logging

class OneMap:
    def __init__(self, api, postal_code_lst):
        self.api = api
        self.postal_code_lst = postal_code_lst
    
    def get_postal_code_url(self, postal_code):
        return self.api.replace('{ searchVal }', postal_code)

    @limits(calls=CALLS_PER_MINUTE, period=MINUTE)    
    def get_lng_lat(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }

        for url in self.postal_code_lst:
            current_url = self.get_postal_code_url(url)
            response = requests.get(current_url, headers=headers, stream=True, timeout=3, allow_redirects=False)

            if response.status_code == 200:
                result = json.loads(response.text)
                if result['totalNumPages'] > 0:
                    output = {
                        'lat' : result['results'][0]['LATITUDE'],
                        'lng' : result['results'][0]['LONGITUDE']
                    }
                    logging.info(output)
                    yield output
                else:
                    logging.warning(f"{url} has no result")
            else:
                logging.warning(f"{url} has status {response.status_code}!")