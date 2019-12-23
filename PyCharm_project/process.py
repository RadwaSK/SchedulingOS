
class Process:
    def __init__(self, id, AT, BT, P):
        self.id = int(id)
        self.AT = int(AT)
        self.BT = int(BT)
        self.P = int(P)
        self.startT = -1
        self.finishT = -1
        self.remainingT = self.BT
        self.periods = []
        self.WT = -1

    def setStartTime(self, time):
        self.WT = float(time) - self.AT
        self.startT = float(time)

    def setFinishTime(self, time):
        self.finishT = float(time)

    def calcTAT(self):
        self.TAT = float(self.finishT) - self.AT

    def calcWTAT(self):
        self.WTAT = round((self.finishT - self.AT) / float(self.BT), 2)

    def getAT(self):
        return self.AT
    
    def getWTAT(self):
        return self.WTAT

    def getExecutionPeriods(self):
        return self.periods

    def addPeriod(self, period):
        self.periods.append(period)

    def execute(self, time, quantum=None):
        if quantum is None:
            quantum = self.BT
        self.addPeriod((time, time+quantum))
        self.remainingT -= quantum
        self.remainingT = max(self.remainingT, 0)

        if self.remainingT == 0:
            self.setFinishTime(time+quantum)
            self.calcTAT()
            self.calcWTAT()

        return self.remainingT

    def printSelf(self, outFile):
        outFile.write("Process #" + str(self.id) + " info.: Waiting Time = "
                      + str(self.WT) + " Turnaround Time = " + str(self.TAT)
                      + " Weighted Turnaround Time = " + str(self.WTAT) + '\n')

