"""Module with definition of Problem interface"""

class Problem(object):
    

    def __init__(self):
        self.max_objective = None
        self.min_objecive = None
        self.problem_type = None
        
    def generateIndividual(self):
        
        raise NotImplementedError
        
    def calculate_objectives(self, individual):
        
        raise NotImplementedError
        
    def fill_individual(self, individual):
        
        raise NotImplementedError