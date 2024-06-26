import sys
import os
import logging
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

from application.services.infrastructure.database_service import DatabaseService

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

        except ValueError as err:
            logging.error(f"ValueError raised {err}")
            return {"error":"wrong parameters please check your values"}
        except Exception as err:
            logging.error(f"Exception raised {err}")
            return {"error":"something went wrong - insert request in db aborted"}

    """delete request from database by id, token or request data

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param id: id in database
        :type id: int
        :param token: identifiyer for user 
        :type token: str
        :param request: request inserted into db
        :type reuest: str or json
        :returns: affected rows count
    """
    def delete_request(self, id = "", token = "", request = ""):
        try:
            query = ""
            params = []
            if id != "":
                query = "DELETE FROM request WHERE id = %s;"
                params = [id]
            if token != "":
                query = "DELETE FROM request WHERE session_id = %s;"
                params = [token]
            if request != "":
                query = "DELETE FROM request WHERE request = %s;"
                params = [token]

            return self.execute_sql(query, params)
        except Exception as err:
            logging.error(f"Exception raised {err}")
            return {"error":f"something went wrong - delete request from db aborted. error: {err}"}

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
            if session_id != "":
                query = "INSERT INTO carbon_score (carbon_g, carbon_kg, carbon_lb, carbon_mt, session_id) VALUES(%s,%s,%s,%s,%s)"
                params = [carbon_g, carbon_kg, carbon_lb, carbon_mt, session_id]
                return self.execute_sql(query, params)
            raise ValueError()
        except ValueError as err:
            logging.error(f"ValueError raised {err}")
            return {"error":"No Session Id specified on insert carbon score into db"}
        except Exception as err:
            logging.error(f"Exception raised {err}")
            return {"error":f"something went wrong - insert carbon score into db message: {err}"}

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
            query = ""
            params = []
            if id != None:
                query = "DELETE FROM carbon_score WHERE id = %s;"
                params = [id]
            if token != None:
                query = "DELETE FROM carbon_score WHERE session_id = %s;"
                params = [token]
            return self.execute_sql(query, params)
        except Exception as err:
            logging.error(f"Exception raised {err}")
            return {"error":f"something went wrong - delete carbon score from db message: {err}"}

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

            if token != None:
                params = [token]
                score = self.execute_sql(query, params)
                return score[0][0]
            raise ValueError()
        except ValueError as err:
            logging.error(f"ValueError raised {err}")
            return {"error":"missing token"}
        except Exception as err:
            logging.error(f"Exception raised {err}")
            return {"error":f"something went wrong - sum carbon score from db err: {err}"}
            
