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
        self.base_url = "https://api.spacetraders.io/v2"
        self.token = os.getenv('SPACETRADERS_AGENT_TOKEN')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Authorization': f"Bearer {self.token}"
        }

    def _get(self, endpoint, resource_id=None):
        url = f"{self.base_url}/{endpoint}"
        if resource_id is not None:
            resource_id = resource_id.replace('"', '')
            url = f"{url}/{resource_id}"

        response = requests.get(url, headers=self.headers)

        if response.status_code >= 400:
            logging.error(f"HTTP {response.status_code}: {url}: {response.content}")
            return b""

        return response.content

    def agent(self, agent_id=None):
        endpoint = "my/agent" if agent_id is None else "agents"
        return self._get(endpoint, agent_id)

    def agents(self):
        return self._get("agents")

    def ships(self, ship_id=None):
        endpoint = "my/ships" if ship_id is None else f"my/ships/{ship_id}"
        return self._get(endpoint, ship_id)

    def systems(self, system_id=None):
        return self._get("systems", system_id)

    def server(self):
        return self._get("")
