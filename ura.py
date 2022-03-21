from config import OUTPUT_CSV_DIR, OUTPUT_CSV_DEL
from constants import HEADER

import urllib3
import requests
import json
import logging
import os
import csv
from urllib3.exceptions import InsecureRequestWarning
from datetime import datetime

urllib3.disable_warnings(InsecureRequestWarning)

class URA:
    def __init__(self, api, lng_lat_lst):
        self.api = api
        self.lng_lat_lst = lng_lat_lst
    
    def get_ura_url(self, lng, lat):
        return self.api.replace('{ lat }', lat).replace('{ lng }', lng)

    def get_ura(self):
        for lng_lat in self.lng_lat_lst:
            postal_code = lng_lat['postal_code']
            lng = lng_lat['lng']
            lat = lng_lat['lat']

            current_url = self.get_ura_url(lng=lng, lat=lat)
            response = requests.get(current_url, headers=HEADER, verify=False)

            if response.status_code == 200:
                result = json.loads(response.text)
                if result['features']:
                    region = result['features'][0]['attributes']['REGION_N'].title()
                    area = result['features'][0]['attributes']['PLN_AREA_N'].title()
                    subzone = result['features'][0]['attributes']['SUBZONE_N'].title()

                    output = {
                        'postal_code' : postal_code,
                        'lat' : lat,
                        'lng' : lng,
                        'region' : region,
                        'area' : area,
                        'subzone' : subzone
                    }
                    logging.info(output)
                    yield output
                else:
                    logging.warning(f"lng={lng} lat={lat} has no result.")
            else:
                logging.warning(f"lng={lng} lat={lat} has status {response.status_code}!")

    def export_to_csv(self, data):
        if not os.path.exists(os.path.dirname(OUTPUT_CSV_DIR)):
            os.mkdir(os.path.dirname(OUTPUT_CSV_DIR))

        output_extension = os.path.splitext(OUTPUT_CSV_DIR)[-1]
        output_csv = OUTPUT_CSV_DIR.replace(output_extension, f"_{datetime.now().strftime('%Y%m%d%H%M%S')}{output_extension}")
        with open(output_csv, 'w', newline='') as csvfile:
            headers = ['postal_code', 'lat', 'lng', 'region', 'area', 'subzone']
            csv_writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=OUTPUT_CSV_DEL)

            csv_writer.writeheader()
            csv_writer.writerows(data)