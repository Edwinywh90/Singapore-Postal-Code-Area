#! /Users/edwinyap/Documents/code/Singapore Postal Code Area/venv/bin/python3

"""
python3 -m venv venv
source venv/bin/activate
pip freeze > requirements.txt
instead of loop through 000000 ~ 999999
find out how postal code structure works : https://www.ura.gov.sg/realEstateIIWeb/resources/misc/list_of_postal_districts.htm
create list of prefix and loop from 0000 to 9999
as onemap limits 250 requests per minutes https://www.onemap.gov.sg/docs/
implement rate limit https://pypi.org/project/ratelimit/

"""
import logging
# from unittest import skip
from constants import *
from config import *
from postal_code import PostalCode
from one_map import OneMap
from datetime import datetime

# import http.client
# http.client.HTTPConnection.debuglevel = 1

# logger = getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(
            filename=f"log/postal_code_{datetime.now().strftime('%F %X')}.log",
            format= "%(levelname)s %(asctime)s %(filename)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.INFO
    )
    # logging.getLogger().setLevel(logging.DEBUG)
    # requests_log = logging.getLogger("requests.packages.urllib3")
    # requests_log.setLevel(logging.DEBUG)
    # requests_log.propagate = True

    postal = PostalCode(prefix_url=POSTAL_CODE_PREFIX_URL,
                        suffix_range=POSTAL_CODE_SUFFIX_RANGE,
                        suffix_leading_zero_len=POSTAL_CODE_SUFFIX_LEADING_ZERO)

    postal.get_valid_postal_code_prefix_from_url()
    postal_code = postal.get_postal_code()

    # if EXPORT_TO_CSV:
    #     postal.export_postal_code_to_csv(postal_code)

    om = OneMap(api=ONE_MAP_API, postal_code_lst=postal_code)
    lng_lat = om.get_lng_lat()

    for i in lng_lat:
        print(i)