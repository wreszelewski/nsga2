import os
import matplotlib.pyplot as pyplot

class Plotter():
    def __init__(self, problem):
        self.problem = problem

    def plot_population_best_front(self, population, generation_number):
        if generation_number % 10 == 0:
            directory = 'plots'
            filename = "{}/generation{}.png".format(directory, str(generation_number))
            self.__create_directory_if_not_exists(directory)
            computed_pareto_front = population.fronts[0]
            self.__plot_front(computed_pareto_front, filename)

    def __create_directory_if_not_exists(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def __plot_front(self, front, filename):
        figure = pyplot.figure()
        axes = figure.add_subplot(111)

        computed_f1 = map(lambda individual: individual.objectives[0], front)
        computed_f2 = map(lambda individual: individual.objectives[1], front)
        axes.plot(computed_f1, computed_f2, 'g.')

        perfect_pareto_front_f1 = seq(0, 1, 0.02)
        perfect_pareto_front_f2 = self.problem.perfect_pareto_front_f2(perfect_pareto_front_f1)
        axes.plot(perfect_pareto_front_f1, perfect_pareto_front_f2, 'r.')

        axes.set_xlabel('f1')
        axes.set_ylabel('f2')
        axes.set_title('Computed Pareto front')
        pyplot.savefig(filename)
        pyplot.close(figure)

def seq(start, stop, step=1):
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    else:
        return([])
