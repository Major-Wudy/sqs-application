import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

from application.services.infrastructure.database_service import DatabaseService
from array import *

"""Instrastructure Service Interface Database

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param DatabaseService: Database service with abstract methods 
    :type DatabaseService: DatabaseService
"""
class DatabaseServiceInterface(DatabaseService):
    """insert request into Database

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param request: request from api to save for unsucceded call to do it later
        :type request: json
        :param session_id: identifyer for user
        :type session_id: str
        :returns: affected rows count
   """
    def insert_request(self, request, session_id):
        try:
            if request == "":
                raise ValueError()
            if session_id == "":
                raise ValueError()

            query = "INSERT INTO request (request, session_id) VALUES (%s, %s);"
            return self.execute_sql(query, [request, session_id])

        except ValueError as verr:
            print(verr)
        except Exception as err:
            print(err)
    """delete request from database by id, token or request data

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param table: database table name
        :type table: str
        :param params: Where clause of your delete statement key value pairs column as key condition as value 
        :type params: array
        :returns: affected rows count
    """
    def delete_request(self, id = "", token = "", request = ""):
        try:
            if not id == "":
                query = "DELETE FROM request WHERE id = %s;"
                params = [id]
            if not token == "":
                query = "DELETE FROM request WHERE session_id = %s;"
                params = [token]
            if request == "":
                query = "DELETE FROM request WHERE request = %s;"
                params = [token]

            return self.execute_sql(query, params)
        except Exception as err:
            print(err)

    """insert carbon score into database

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
        :returns: affected rows count
    """
    def insert_carbon_score(self, carbon_g = 0, carbon_kg = 0, carbon_lb = 0, carbon_mt = 0, session_id = ""):
        try:
            query = "INSERT INTO carbon_score (carbon_g, carbon_kg, carbon_lb, carbon_mt, session_id) VALUES(%s,%s,%s,%s,%s)"
            params = [carbon_g, carbon_kg, carbon_lb, carbon_mt, session_id]
            return self.execute_sql(query, params)
        except Exception as err:
            print(err)

    """delete specific carbon score by id or all for one user by token

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param id: Id of your database entry
        :type id: int
        :param token: identifiyer for all scores per user
        :type token: str
        :returns: affected rows count
    """
    def delete_carbon_score(self, id=None, token=None):
        try:
            if not id == None:
                query = "DELETE FROM carbon_score WHERE id = %s;"
                params = [id]
            if not token == None:
                query = "DELETE FROM carbon_score WHERE session_id = %s;"
                params = [token]
            return self.execute_sql(query, params)
        except Exception as err:
            print(err)

    """ sum up carbon score for one user

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param token: token of the needed user (identifyer)
        :type token: str or None
        :param unit: retrived score as gramms g, kilogramms kg, pounds lb, megatons mt
        :type unit: str
        :returns: sum of selected column
    """
    def sum_carbon_score_for_session_id(self, token=None, unit="g"):
        try:
            match unit:
                case "g":
                    query = "SELECT SUM(carbon_g) FROM carbon_score WHERE session_id = %s;"
                case "kg":
                    query = "SELECT SUM(carbon_kg) FROM carbon_score WHERE session_id = %s;"
                case "lb":
                    query = "SELECT SUM(carbon_lb) FROM carbon_score WHERE session_id = %s;"
                case "mt":
                    query = "SELECT SUM(carbon_mt) FROM carbon_score WHERE session_id = %s;"

            if not token == None:
                params = [token]
                score = self.execute_sql(query, params)
                return score[0][0]
        except Exception as err:
            print(err)
