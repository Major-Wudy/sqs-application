import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

import requests
from dotenv import load_dotenv
load_dotenv()

class CarbonInterfaceRequestService:
    base_url = "https://www.carboninterface.com/api/v1/auth"
    api_key = os.environ.get('API_KEY')
    def auth_request(cls):
        headers = {'Authorization': 'Bearer ' + cls.api_key}
        r = requests.get(cls.base_url, headers=headers)

        print(r.text)