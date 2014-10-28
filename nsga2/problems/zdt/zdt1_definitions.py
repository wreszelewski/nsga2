import math
from nsga2 import seq
from nsga2.problems.problem_definitions import ProblemDefinitions

class ZDT1Definitions(ProblemDefinitions):

    def __init__(self):
        self.n = 30

    def f1(self, individual):
        return individual.features[0]

    def f2(self, individual):
        sigma = sum(individual.features[1:])
        g = 1 + sigma*9/(self.n - 1)
        h = 1 - math.sqrt(self.f1(individual)/g)
        return g*h

    def perfect_pareto_front(self):
        domain = seq(0, 1, 0.01)
        return domain, map(lambda x1: 1 - math.sqrt(x1), domain)
