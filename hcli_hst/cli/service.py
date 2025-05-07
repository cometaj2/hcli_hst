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

    def agent(self, agent_id=None):
        SPACETRADERS_TOKEN = os.getenv('SPACETRADERS_AGENT_TOKEN')

        url = f"https://api.spacetraders.io/v2/my/agent"
        if agent_id is not None:
            agent_id = agent_id.replace('"', '')
            url = f"https://api.spacetraders.io/v2/agents/{agent_id}"

        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Authorization' : f"Bearer {SPACETRADERS_TOKEN}"
        })

        # Check if request was successful
        if response.status_code >= 400:
            logging.error(f"Failed to fetch {url}: HTTP {response.status_code}: {response.content}")
            return b""

        return response.content

    def agents(self):
        SPACETRADERS_TOKEN = os.getenv('SPACETRADERS_AGENT_TOKEN')

        url = f"https://api.spacetraders.io/v2/agents"

        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Authorization' : f"Bearer {SPACETRADERS_TOKEN}"
        })

        # Check if request was successful
        if response.status_code >= 400:
            logging.error(f"Failed to fetch {url}: HTTP {response.status_code}: {response.content}")
            return b""

        return response.content

    def ships(self, ship_id=None):
        SPACETRADERS_TOKEN = os.getenv('SPACETRADERS_AGENT_TOKEN')

        url = f"https://api.spacetraders.io/v2/my/ships"
        if ship_id is not None:
            ship_id = ship_id.replace('"', '')
            url = f"https://api.spacetraders.io/v2/my/ships/{ship_id}"

        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Authorization' : f"Bearer {SPACETRADERS_TOKEN}"
        })

        # Check if request was successful
        if response.status_code >= 400:
            logging.error(f"HTTP {response.status_code}: {url}: {response.content}")
            return b""

        return response.content


    def systems(self, system_id=None):
        SPACETRADERS_TOKEN = os.getenv('SPACETRADERS_AGENT_TOKEN')

        url = "https://api.spacetraders.io/v2/systems"
        if system_id is not None:
            system_id = system_id.replace('"', '')
            url = f"https://api.spacetraders.io/v2/systems/{system_id}"

        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Authorization' : f"Bearer {SPACETRADERS_TOKEN}"
        })

        # Check if request was successful
        if response.status_code >= 400:
            logging.error(f"HTTP {response.status_code}: {url}: {response.content}")
            return b""

        return response.content

    def server(self):
        SPACETRADERS_TOKEN = os.getenv('SPACETRADERS_AGENT_TOKEN')

        url = "https://api.spacetraders.io/v2"

        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Authorization' : f"Bearer {SPACETRADERS_TOKEN}"
        })

        # Check if request was successful
        if response.status_code >= 400:
            logging.error(f"HTTP {response.status_code}: {url}: {response.content}")
            return b""

        return response.content
