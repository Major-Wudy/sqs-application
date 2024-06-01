import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from application.models.carbon.score import Score

from decimal import Decimal

class CarbonService():
    @classmethod
    def create_carbon_score(cls, score_g: Decimal, score_kg: Decimal, score_lb: Decimal, score_mt: Decimal, session_id: str) -> Score:
        try:
            if not isinstance(score_g, Decimal) or not isinstance(score_kg, Decimal) or not isinstance(score_lb, Decimal) or not isinstance(score_mt, Decimal) or not isinstance(session_id, str):
                raise TypeError()
            
            return Score(Decimal(score_g), Decimal(score_kg), Decimal(score_lb), Decimal(score_mt), session_id)
        except TypeError:
            return Score(Decimal(0), Decimal(0), Decimal(0), Decimal(0), "")

    @classmethod
    def convert_score_to_json(cls, score: Score) -> dict:
        try: 
            if not isinstance(score, Score):
                raise TypeError():
            return {
                "carbon_g": str(score.score_g),
                "carbon_kg":str(score.score_kg),
                "carbon_lb":str(score.score_lb),
                "carbon_mt":str(score.score_mt),
                "SessionId":score.session_id,
            }
        except TypeError:
            return {
                "carbon_g": "0",
                "carbon_kg": "0",
                "carbon_lb": "0",
                "carbon_mt": "0",
                "SessionId":"",
            }
