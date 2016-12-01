import os
import matplotlib.pyplot as plt

class Plotter():
    def __init__(self, problem):
        self.directory = 'plots'
        self.problem = problem
        self._f1_lim = None
        self._f2_lim = None

    def plot_population_best_front(self, population, generation_number):
        if generation_number % 10 == 0:
            self.__create_directory_if_not_exists()
            computed_pareto_front = population.fronts[0]
            self.__plot_front(computed_pareto_front, generation_number)

    def plot_x_y(self, x, y, x_label, y_label, title, filename):
        filename = "{}/{}.png".format(self.directory, filename)
        self.__create_directory_if_not_exists()
        figure = plt.figure()
        axes = figure.add_subplot(111)
        axes.plot(x, y, 'r')
        axes.set_xlabel(x_label)
        axes.set_ylabel(y_label)
        axes.set_title(title)
        plt.savefig(filename)
        plt.close(figure)

    def __create_directory_if_not_exists(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def __plot_front(self, front, generation_number):
        filename = "{}/generation{}.png".format(self.directory, str(generation_number))
        figure = plt.figure()
        axes = figure.add_subplot(111)

        computed_f1 = map(lambda individual: individual.objectives[0], front)
        computed_f2 = map(lambda individual: individual.objectives[1], front)
        axes.plot(computed_f1, computed_f2, 'g.')

        if self._f1_lim is None:
            self._f1_lim = max(computed_f1)
        if self._f2_lim is None:
            self._f2_lim = max(computed_f2)

        perfect_pareto_front_f1, perfect_pareto_front_f2 = self.problem.perfect_pareto_front()
        axes.plot(perfect_pareto_front_f1, perfect_pareto_front_f2, 'r.')

        axes.set_xlabel('$f1$')
        axes.set_ylabel('$f2$')
        axes.set_xlim(0,self._f1_lim)
        axes.set_ylim(0,self._f2_lim)
        axes.set_title('$Computed Pareto front @ Epoch {:}$'.format(generation_number))
        plt.savefig(filename)
        plt.legend(loc='upper left')
        plt.close(figure)


