import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

from abc import ABC, abstractmethod
import requests
from dotenv import load_dotenv
load_dotenv()

"""Infrastructure Service Carboninterface RequestServvice
"""
class CarbonInterfaceRequestService(object):
    base_url = os.environ.get('API_BASE_URL')
    url_auth_addon = "auth"
    url_estimates_addon = "estimates"
    api_key = os.environ.get('API_KEY')

    """Authorization headers for request

        :author: Raphael Wudy (raphael.wudy@atud.th-rosenheim.de)
        :returns: Auth headers as dictionary
        :rtype: dict
    """
    @classmethod
    def get_authoriztaion_header(cls) -> dict:
        return {'Authorization': 'Bearer ' + cls.api_key}

    """Authorization & content type json headers for request

        :author: Raphael Wudy (raphael.wudy@atud.th-rosenheim.de)
        :returns: Auth headers as dictionary
        :rtype: dict
    """
    @classmethod
    def get_authorization_and_content_type_header(cls) -> dict:
        return {'Authorization': 'Bearer ' + cls.api_key, 'Content-Type':'application/json'}
    
    """get auth url for carbon interface api

        :author: Raphael Wudy (raphael.wudy@atud.th-rosenheim.de)
        :returns: auth url
        :rtype: str
    """
    @classmethod
    def get_auth_url(cls) -> str:
        return cls.base_url + cls.url_auth_addon

    """get estimate url for carbon interface api

        :author: Raphael Wudy (raphael.wudy@atud.th-rosenheim.de)
        :returns: estimate url
        :rtype: str
    """
    @classmethod
    def get_estimates_url(cls) -> str:
        return cls.base_url + cls.url_estimates_addon
    
    """abstract method up for implementation to post some data against url with headers 

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param url: url for post request
        :type url: str
        :param data: request data as dictionary default none
        :type data: dict
        :param json: request data as json default none
        :type json: dict
        :param headers: headers for your post request default none
        :type headers: dict
        :returns: server response as json
        :rtype: dict
    """
    @abstractmethod
    def post(self, url: str, data: dict = None, json: dict = None, headers: dict = None) -> dict:
        pass

    """abstract method up for implementation to get some data with headers 

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param url: url for post request
        :type url: str
        :param params: request params as dictionary default none
        :type data: dict
        :param headers: headers for your post request default none
        :type headers: dict
        :returns: server response as json
        :rtype: dict
    """
    @abstractmethod
    def get(self, url: str, params: dict = None, headers: dict = None) -> dict:
        pass