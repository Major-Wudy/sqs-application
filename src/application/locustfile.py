import time
import os
from dotenv import load_dotenv
from locust import HttpUser, task, between
from json import JSONDecodeError

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    token = os.environ.get('TOKEN_UNIT_TEST')

    @task
    def create_electricity(self):
        response = self.client.post("api/create/electricity", json={"value":123.45, "country":"us","state":"fl","unit":"kwh"}, headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059'})
        print("Response status code:", response.status_code)