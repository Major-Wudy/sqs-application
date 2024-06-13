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
    def execute_sql(self, query, params=None):
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()
            else:
                return cursor.rowcount

    """abstract method up for implementation to interact with your Database update

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param params: your insert values
        :type params: array
   """
    @abstractmethod
    def insert_requests(self, request, session_id):
        pass

    """abstract method up for implementation to interact with your Database update

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param table: database table name
        :type table: str
        :param updates: Key value array with column as key and update as value 
        :type updates: array
    
    @abstractmethod
    def update(table: str, updates: array):
        pass

    abstract method up for implementation to interact with your Database delete

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param table: database table name
        :type table: str
        :param params: Where clause of your delete statement key value pairs column as key condition as value 
        :type params: array
    """
    @abstractmethod
    def delete_request(params: array):
        pass
    