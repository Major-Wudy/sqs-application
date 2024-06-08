from decimal import Decimal

class Score:
    def __init__(self, score_g, score_kg, score_lb, score_mt, session_id):
        self.score_g = score_g
        self.score_kg = score_kg
        self.score_lb = score_lb
        self.score_mt = score_mt
        self.session_id = session_id