"""NSGA-II related functions"""

import functools
from nsga2.population import Population
import random

class NSGA2Utils(object):
    
    def __init__(self, problem, num_of_individuals):
        
        self.problem = problem
        self.num_of_individuals = num_of_individuals
        
    def fast_nondominated_sort(self, population):
        
        for individual in population:
            individual.domination_count = 0
            individual.dominated_solutions = set()
            
            for other_individual in population:
                if individual.dominates(other_individual):
                    individual.dominated_solutions.add(other_individual)
                elif other_individual.dominates(individual):
                    individual.domination_count += 1
            if individual.domination_count == 0:
                population.fronts[0].append(individual)
                individual.rank = 0
        i = 0
        while len(population.fronts[i]) > 0:
            temp = []
            for individual in population.fronts[i]:
                for other_individual in individual.dominated_solutions:
                    other_individual.domination_count -= 1
                    if other_individual.domination_count == 0:
                        other_individual.rank = i+1
                        temp.append(other_individual)
            i = i+1
            population.fronts[i] = temp
                    
    def __sort_objective(self, m, val1, val2):
        return cmp(val1.objectives[m], val2.objectives[m])
    
    def calculate_crowding_distance(self, front):
        solutions_num = len(front)
        for individual in front:
            individual.crowding_distance = 0
            
        for m in range(len(front[0].objectives)):
            front = sorted(front, cmp=functools.partial(self.__sort_objective, m=m))
            front[0].crowding_distance = self.problem.max_objective[m]
            front[solutions_num-1].crowding_distance = self.problem.max_objective[m]
            for index in enumerate(front[1:solutions_num-1]):
                front[index].crowding_distance = (front[index+1].crowding_distance - front[index-1].crowding_distance) / (self.problem.max_objective[m] - self.problem.min_objective[m])
                
    def crowding_operator(self, individual, other_individual):
        if (individual.rank < other_individual.rank) or \
            ((individual.rank == other_individual.rank) and (individual.crowding_distance > other_individual.crowding_distance)):
            return 1
        else:
            return -1
    
    def create_initial_population(self):
        population = Population()
        for _ in range(self.num_of_individuals):
            individual = self.problem.generateIndividual()
            self.problem.fill_individual(individual)
            self.problem.calculate_objectives(individual)
            population.population.append(self.problem.generateIndividual())
            
        return population
    
    def create_children(self, population):
        pass
    
    def __crossover(self, individual1, individual2):
        child = self.problem.generateIndividual()
        genes_indexes = range(len(child.features))
        half_genes_indexes = random.sample(genes_indexes, self.num_of_individuals)
        for i in genes_indexes:
            if i in half_genes_indexes:
                child.features[i] = (individual1.features[i] + individual2.features[i])/2
            else:
                child.features[i] = individual1.features[i]
        return child
        
    