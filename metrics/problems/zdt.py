from metrics.hvr import HVR, HV

class ZDT1Metrics():
    def HV(self, front):
        return HV([11, 11])(front)

    def HVR(self, front):
        return HVR(120 + 2/3, [11, 11])(front)

class ZDT2Metrics():
    def HV(self, front):
        return HV([11, 11])(front)

    def HVR(self, front):
        return HVR([11, 11], 120 + 1/3)(front)

class ZDT3Metrics():
    def HV(self, front):
        return HV([11, 11])(front)

    def HVR(self, front):
        return HVR([11, 11], 128.77811613069076060)(front)