"""Module with main parts of NSGA-II algorithm.
Contains main loop"""

from nsga2.utils import NSGA2Utils
from nsga2.population import Population

class Evolution(object):
    
    def __init__(self, problem, num_of_generations, num_of_individuals):
        self.utils = NSGA2Utils(problem, num_of_individuals)

        self.population = None
        self.num_of_generations = num_of_generations
        self.on_generation_finished = []
        self.num_of_individuals = num_of_individuals
    
    def register_on_new_generation(self, fun):
        self.on_generation_finished.append(fun)
        
    def evolve(self):
        
        self.population = self.utils.create_initial_population()
        self.utils.fast_nondominated_sort(self.population)
        for front in self.population.fronts:
            self.utils.calculate_crowding_distance(front)
        children = self.utils.create_children(self.population)
        returned_population = None 
        for i in range(self.num_of_generations):
            self.population.extend(children)
            self.utils.fast_nondominated_sort(self.population)
            new_population = Population()
            front_num = 0
            while len(new_population) + len(self.population.fronts[front_num]) <= self.num_of_individuals:
                self.utils.calculate_crowding_distance(self.population.fronts[front_num])
                new_population.extend(self.population.fronts[front_num])
                front_num += 1
                
            sorted(self.population.fronts[front_num], cmp=self.utils.crowding_operator)
            new_population.extend(self.population.fronts[front_num][0:self.num_of_individuals-len(new_population)])
            returned_population = self.population
            self.population = new_population
            children = self.utils.create_children(self.population)
            for fun in self.on_generation_finished:
                fun(returned_population, i)
        return returned_population.fronts[0]
                
                
            
            
