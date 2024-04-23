import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

from abc import ABC, abstractmethod
import requests
from dotenv import load_dotenv
load_dotenv()

class CarbonInterfaceRequestService(object):
    base_url = "https://www.carboninterface.com/api/v1/"
    url_auth_addon = "auth"
    url_estimates_addon = "estimates"
    api_key = os.environ.get('API_KEY')

    def auth_request(self):
        try:
            headers = self.get_authoriztaion_header()
            url = self.base_url + self.url_auth_addon
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print(response.text)

    @classmethod
    def get_authoriztaion_header(self) -> dict:
        return {'Authorization': 'Bearer ' + self.api_key}

    @classmethod
    def get_authorization_and_content_type_header(self) -> dict:
        return {'Authorization': 'Bearer ' + self.api_key, 'Content-Type':'application/json'}
    
    @classmethod
    def get_auth_url(self) -> str:
        return self.base_url + self.url_auth_addon

    @classmethod
    def get_estimates_url(self) -> str:
        return self.base_url + self.url_estimates_addon
        
    @abstractmethod
    def post(self, url: str, data: dict = None, json: dict = None, headers: dict = None) -> dict:
        """
        Führt eine HTTP-POST-Anfrage an die angegebene URL aus und gibt die Antwortdaten zurück.

        Args:
            url (str): Die URL, an die die POST-Anfrage gesendet werden soll.
            data (dict, optional): Optionale Daten, die mit der Anfrage gesendet werden sollen (für Formulardaten).
            json (dict, optional): Optionale JSON-Daten, die mit der Anfrage gesendet werden sollen.
            headers (dict, optional): Optionale Header, die an die Anfrage angehängt werden sollen.

        Returns:
            dict: Die Antwortdaten als Python-Datenstruktur (z. B. ein JSON-Objekt).
        """
        pass

    @abstractmethod
    def get(self, url: str, params: dict = None, headers: dict = None) -> dict:
        """
        Führt eine HTTP-GET-Anfrage an die angegebene URL aus und gibt die Antwortdaten zurück.

        Args:
            url (str): Die URL, an die die GET-Anfrage gesendet werden soll.
            params (dict, optional): Optionale Parameter, die an die Anfrage angehängt werden sollen.
            headers (dict, optional): Optionale Header, die an die Anfrage angehängt werden sollen.

        Returns:
            dict: Die Antwortdaten als Python-Datenstruktur (z. B. ein JSON-Objekt).
        """
        pass