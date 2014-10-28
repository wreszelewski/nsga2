from nsga2.evolution import Evolution
from nsga2.problems.zdt import ZDT
from nsga2.problems.zdt1_definitions import ZDT1Definitions
from nsga2.problems.zdt2_definitions import ZDT2Definitions
from nsga2.problems.zdt3_definitions import ZDT3Definitions
from plotter import Plotter

def print_generation(population, generation_num):
    print("Generation: {}".format(generation_num))

zdt1_definitions = ZDT3Definitions()
plotter = Plotter(zdt1_definitions)
problem = ZDT(zdt1_definitions)
evolution = Evolution(problem, 300, 100)
evolution.register_on_new_generation(plotter.plot_population_best_front)
evolution.register_on_new_generation(print_generation)
pareto_front = evolution.evolve()

