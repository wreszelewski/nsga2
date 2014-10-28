def HV(reference_point):
    def calculate_hyper_volume(front):
        def volume(individual):
            hyper_cuboid_sides = []
            for i in range(len(reference_point)):
                side_length = abs(individual.objectives[i] - reference_point[i])
                hyper_cuboid_sides.append(side_length)
            return reduce(lambda x, y: x*y, hyper_cuboid_sides, 1)

        return reduce(lambda sum, individual: sum + volume(individual), front, 0) / len(front)
    return calculate_hyper_volume

def HVR(reference_point, max_hyper_volume):
    def calculate_hyper_volume_rate(front):
        return HV(reference_point)(front) / max_hyper_volume
    return calculate_hyper_volume_rate
