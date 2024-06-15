import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

from django.db import connection
from abc import ABC, abstractmethod
from array import *

"""Infrastructure Service Database Service

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
"""
class DatabaseService():
    """execute sql queries

        :author: Raphael Wudy (raphae.wudy@stud.th-rosenheim.de)
        :param query: sql query for execution
        :type query: str
        :param params: Array of your params default is none
        :type params: array or None
        :returns: database entries on select or affected rows by update, delete, insert
    """
    def execute_sql(self, query, params=None):
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()
            else:
                return cursor.rowcount

    """abstract method up for implementation to interact with your Database update

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param request: request from api to save for unsucceded call to do it later
        :type request: json
        :param session_id: identifyer for user
        :type session_id: str
   """
    @abstractmethod
    def insert_requests(self, request, session_id):
        pass

    """abstract method up for implementation to interact with your Database delete

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param table: database table name
        :type table: str
        :param params: Where clause of your delete statement key value pairs column as key condition as value 
        :type params: array
        :returns: affected rows count
    """
    @abstractmethod
    def delete_request(self, id = "", token = "", request = ""):
        pass

    """abstract method up for implementation insert carbon scores into database

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param carbon_g: carbon pollution in gramms
        :type carbon_g: decimal
        :param carbon_kg: carbon pollution in kilogramms
        :type carbon_kg: decimal
        :param carbon_lb: carbon pollution in pounds
        :type carbon_lb: decimal
        :param carbon_mt: carbon pollution in megatons
        :type carbon_mt: decimal
        :param session_id: identifyer for user etc. in database
        :type session_id: str
    """
    @abstractmethod
    def insert_carbon_score(self, carbon_g, carbon_kg, carbon_lb, carbon_mt, session_id):
        pass

    """ abstractmethod up for implementation delete carbon score for user or specific one

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param id: Id of your database entry
        :type id: int
        :param token: identifiyer for all scores per user
        :type token: str
    """
    @abstractmethod
    def delete_carbon_score(self, id, token):
        pass
    