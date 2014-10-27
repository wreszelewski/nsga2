import os
import matplotlib.pyplot as pyplot
from math import sqrt

class Plotter():
    def plotPopulationBestFront(self, population, generationNumber):
        if generationNumber % 10 == 0:
            directory = 'plots'
            filename = "{}/generation{}.png".format(directory, str(generationNumber))
            self.createDirectoryIfNotExists(directory)
            computedParetoFront = population.fronts[0]
            self.plotFront(computedParetoFront, filename)

    def createDirectoryIfNotExists(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def plotFront(self, front, filename):
        figure = pyplot.figure()
        axes = figure.add_subplot(111)
        computedF1 = map(lambda individual: individual.objectives[0], front)
        computedF2 = map(lambda individual: individual.objectives[1], front)
        perfectParetoFrontX1 = seq(0, 1, 0.02)
        perfectParetoFrontX2 = map(lambda x1: 1 - sqrt(x1), perfectParetoFrontX1)
        axes.plot(computedF1, computedF2, 'g.')
        axes.plot(perfectParetoFrontX1, perfectParetoFrontX2, 'r.')
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
