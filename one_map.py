from constants import HEADER

import urllib3
import requests
import json
import logging
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)
class OneMap:
    def __init__(self, api, postal_code_lst):
        self.api = api
        self.postal_code_lst = postal_code_lst
    
    def get_postal_code_url(self, postal_code):
        return self.api.replace('{ searchVal }', postal_code)

    def get_lng_lat(self):
        for postal_code in self.postal_code_lst:
            current_url = self.get_postal_code_url(postal_code)
            response = requests.get(current_url, headers=HEADER, stream=True, allow_redirects=False, verify=False)

            if response.status_code == 200:
                result = json.loads(response.text)
                if result['totalNumPages'] > 0:
                    output = {
                        'postal_code' : postal_code,
                        'lat' : result['results'][0]['LATITUDE'],
                        'lng' : result['results'][0]['LONGITUDE']
                    }
                    logging.info(output)
                    yield output
                else:
                    logging.warning(f"{postal_code} has no result.")
            else:
                logging.warning(f"{postal_code} has status {response.status_code}!")