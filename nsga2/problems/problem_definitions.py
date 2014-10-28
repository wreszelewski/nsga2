class ProblemDefinitions():

    def __init__(self):
        raise NotImplementedError

    def f1(self, individual):
        raise NotImplementedError

    def f2(self, individual):
        raise NotImplementedError

    def perfect_pareto_front_f2(self, perfect_pareto_front_f1):
        raise NotImplementedError