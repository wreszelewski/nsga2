"""Module with main parts of NSGA-II algorithm.
It contains individual definition"""

class Individual(object):
    """Represents one individual"""
    
    def __init__(self, features):
        self.rank = None
        self.crowding_distance = None
        self.dominated_solutions = set()
        self.features = features
        self.objectives = None
        
    def set_objectives(self, objectives):
        self.objectives = objectives
        
