import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

from application.services.infrastructure.database_service import DatabaseService
from array import *

class DatabaseServiceInterface(DatabaseService):
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

    def delete_request(self, id = "", token = ""):
        try:
            if not id == "":
                query = "DELETE FROM request WHERE id = %s;"
                params = [id]
            if not token == "":
                query = "DELETE FROM request WHERE session_id = %s;"
                params = [token]

            return self.execute_sql(query, params)
        except Exception as err:
            print(err)

    def insert_carbon_score(self, carbon_g = 0, carbon_kg = 0, carbon_lb = 0, carbon_mt = 0, session_id = ""):
        try:
            query = "INSERT INTO carbon_score (carbon_g, carbon_kg, carbon_lb, carbon_mt, session_id) VALUES(%s,%s,%s,%s,%s)"
            params = [carbon_g, carbon_kg, carbon_lb, carbon_mt, session_id]
            return self.execute_sql(query, params)
        except Exception as err:
            print(err)