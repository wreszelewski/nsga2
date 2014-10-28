"""Module with definition of Problem interface"""

from nsga2.individual import Individual
from nsga2.problems import Problem
import random
import functools
import math

class ZDT2(Problem):
    

    def __init__(self):
        self.max_objectives = [None, None]
        self.min_objectives = [None, None]
        self.problem_type = None

    def __dominates(self, individual2, individual1):
        worse_than_other = self.__f1(individual1) <= self.__f1(individual2) and self.__f2(individual1) <= self.__f2(individual2)
        better_than_other = self.__f1(individual1) < self.__f1(individual2) or self.__f2(individual1) < self.__f2(individual2)
        return worse_than_other and better_than_other
        
    def generateIndividual(self):
        
        individual = Individual()
        individual.features = []
        for i in range(30):
            individual.features.append(random.random())
        individual.dominates = functools.partial(self.__dominates, individual1=individual)
        self.calculate_objectives(individual)
        return individual
        
    def calculate_objectives(self, individual):
        individual.objectives = []
        individual.objectives.append(self.__f1(individual))
        individual.objectives.append(self.__f2(individual))
        for i in range(2):
            if self.min_objectives[i] is None or individual.objectives[i] < self.min_objectives[i]:
                self.min_objectives[i] = individual.objectives[i] 
            if self.max_objectives[i] is None or individual.objectives[i] > self.max_objectives[i]:
                self.max_objectives[i] = individual.objectives[i] 

    def __f1(self, individual):
        return individual.features[0]

    def __f2(self, individual):
        sigma = sum(individual.features[1:])
        g = 1 + sigma*9/(29)
        h = 1 - (individual.features[0]/g)*(individual.features[0]/g)
        return g*h
        
        
        
