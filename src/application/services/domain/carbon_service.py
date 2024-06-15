import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from application.models.carbon.score import Score
from decimal import Decimal
import logging

"""Domain Service CarbonService

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
"""
class CarbonService():
    """create carbon score entity

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param score_g: estimated carbon score in gramms
        :type score_g: Decimal
        :param score_kg: estimated carbon score in kilo gramms
        :type score_kg: Decimal
        :param score_lb: estimated carbon score in pounds
        :type score_lb: Decimal
        :param score_mt: estimated carbon score in mega tons
        :type score_mt: Decimal
        :param session_id: user session id or auth token
        :type session_id: str
        :returns: Score
        :rtype: Score
    """
    @classmethod
    def create_carbon_score(cls, score_g: Decimal, score_kg: Decimal, score_lb: Decimal, score_mt: Decimal, session_id: str) -> Score:
        try:
            if not isinstance(score_g, Decimal) or not isinstance(score_kg, Decimal) or not isinstance(score_lb, Decimal) or not isinstance(score_mt, Decimal) or not isinstance(session_id, str):
                raise TypeError()
            
            return Score(Decimal(score_g), Decimal(score_kg), Decimal(score_lb), Decimal(score_mt), session_id)
        except TypeError as err:
            logging.error(f"TypeError raised {err}")
            return Score(Decimal(0), Decimal(0), Decimal(0), Decimal(0), "")

    """converts given Carbon Score Entity to json

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param score: Score entity
        :type score: Score
        :returns: dictionary
        :rtype: dict
    """
    @classmethod
    def convert_score_to_json(cls, score: Score) -> dict:
        try: 
            if not isinstance(score, Score):
                raise TypeError()
            return {
                "carbon_g": str(score.score_g.quantize(Decimal('0.01'))),
                "carbon_kg":str(score.score_kg.quantize(Decimal('0.01'))),
                "carbon_lb":str(score.score_lb.quantize(Decimal('0.01'))),
                "carbon_mt":str(score.score_mt.quantize(Decimal('0.01'))),
                "sessionId":score.session_id,
            }
        except TypeError as err:
            logging.error(f"TypeError raised {err}")
            return {
                "carbon_g": "0",
                "carbon_kg": "0",
                "carbon_lb": "0",
                "carbon_mt": "0",
                "sessionId":"",
            }
