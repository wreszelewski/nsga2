from nsga2.evolution import Evolution
from nsga2.problems.zdt1 import ZDT1
from plotter import Plotter

plotter = Plotter()
zdt1 = ZDT1()
evolution = Evolution(zdt1, 10, 30)
evolution.register_on_new_generation(plotter.plotPopulationBestFront)
pareto_front = evolution.evolve()


