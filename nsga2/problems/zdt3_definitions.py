import math
from nsga2.problems.problem_definitions import ProblemDefinitions

class ZDT3Definitions(ProblemDefinitions):

    def __init__(self):
        self.n = 30

    def f1(self, individual):
        return individual.features[0]

    def f2(self, individual):
        sigma = sum(individual.features[1:])
        g = 1 + sigma*9/(self.n - 1)
        f1 = self.f1(individual)
        h = 1 - math.sqrt(f1/g) - (f1/g)*math.sin(10*math.pi*f1)
        return g*h

    def perfect_pareto_front_f2(self, perfect_pareto_front_f1):
        return map(lambda x1: 1 - math.sqrt(x1) - x1*math.sin(10*math.pi*x1), perfect_pareto_front_f1)