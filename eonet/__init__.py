import os

from dotenv import load_dotenv
import requests_cache
from requests.auth import HTTPBasicAuth


load_dotenv()
API_KEY = os.environ.get('API_KEY')

session = requests_cache.CachedSession('http_cache', auth=HTTPBasicAuth('apikey', API_KEY), backend='filesystem')
session.params = {}

from .api import EONET