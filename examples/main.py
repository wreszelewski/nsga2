from nsga2.evolution import Evolution
from nsga2.problems.zdt1 import ZDT1
from plotter import Plotter


def print_generation(population, generation_num):
    print("Generation: {}".format(generation_num))

plotter = Plotter()
zdt1 = ZDT1()
evolution = Evolution(zdt1, 300, 100)
evolution.register_on_new_generation(plotter.plotPopulationBestFront)
evolution.register_on_new_generation(print_generation)
pareto_front = evolution.evolve()



