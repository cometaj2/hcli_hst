import io
import sys
import os
import re
import time
import inspect
import logger
import requests
from urllib.parse import urljoin, urlparse

from datetime import datetime

from hcli_problem_details import *

logging = logger.Logger()


class Service:

    def __init__(self):
        return

    def ship_status(self, ship_id):

        ship_id = "HCLI_CORE-3"
        url = f"https://api.spacetraders.io/v2/my/ships/{ship_id}"

        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Authorization' : "Bearer $SPACETRADERS_TOKEN"
        })

        # Check if request was successful
        if response.status_code >= 400:
            logging.error(f"Failed to fetch {url}: Status code {response.status_code}")
            return None

        return response.content
