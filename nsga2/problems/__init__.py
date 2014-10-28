"""Module with definition of Problem interface"""

class Problem(object):
    
    def __init__(self):
        self.max_objectives = None
        self.min_objecives = None
        self.problem_type = None
        
    def generateIndividual(self):
        
        raise NotImplementedError
        
    def calculate_objectives(self, individual):
        
        raise NotImplementedError
