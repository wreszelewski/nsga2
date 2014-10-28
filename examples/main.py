from metrics.problems.zdt import ZDT3Metrics
from nsga2.evolution import Evolution
from nsga2.problems.zdt import ZDT
from nsga2.problems.zdt.zdt3_definitions import ZDT3Definitions
from plotter import Plotter

def print_generation(population, generation_num):
    print("Generation: {}".format(generation_num))

def print_metrics(population, generation_num):
    pareto_front = population.fronts[0]
    zdt3_metrics = ZDT3Metrics()
    hv = zdt3_metrics.HV(pareto_front)
    hvr = zdt3_metrics.HVR(pareto_front)
    print("HV: {}".format(hv))
    print("HVR: {}".format(hvr))

zdt3_definitions = ZDT3Definitions()
plotter = Plotter(zdt3_definitions)
problem = ZDT(zdt3_definitions)
evolution = Evolution(problem, 100, 100)
evolution.register_on_new_generation(plotter.plot_population_best_front)
evolution.register_on_new_generation(print_generation)
evolution.register_on_new_generation(print_metrics)
pareto_front = evolution.evolve()
