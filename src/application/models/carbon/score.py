from decimal import Decimal

class Score:
    def __init__(self, score_g, score_kg, score_lb, score_mt, session_id):
        self.score_g = Decimal(score_g)
        self.score_kg = Decimal(score_kg)
        self.score_lb = Decimal(score_lb)
        self.score_mt = Decimal(score_mt)
        self.session_id = session_id