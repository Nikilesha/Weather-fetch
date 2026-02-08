import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
from dotenv import load_dotenv
import os


load_dotenv()

cache_session = requests_cache.CachedSession('.cache',expire_After=3600)
retry_session = retry(cache_session,retries=3,backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

url = os.getenv('URL')
lat = os.getenv('LATITUDE')
lon = os.getenv('LONGITUDE')
par = {
    'latitude': lat,
    'longitude': lon,
    'hourly': 'temperature_2m',
}

cache_dir = "cache"
raw_data_dir = "data/raw"
log_dir = "logs"

