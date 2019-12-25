from process import *

def WriteLog(processes, algorithm_name):
    file_name = algorithm_name + '_Log.txt'
    # this opens a new file
    temp = open(file_name, 'w')
    # with this object I can append to file
    logFile = open(file_name, 'a')
    n = len(processes)

    av_TAT = 0
    av_WTAT = 0
    for p in processes:
        av_TAT += p.getAT()
        av_WTAT += p.getWTAT()

    av_TAT /= float(n)
    av_WTAT /= float(n)

    logFile.write("Average Turnaround Time = " + str(av_TAT) + '\n')
    logFile.write("Average Weighted Turnaround Time = " + str(av_WTAT) + '\n')

    for p in processes:
        p.printSelf(logFile)


def getLists(processes, contextList):
    periods = []
    for p in processes:
        periods.append([p.id, p.getExecutionPeriods()])

    periods.sort(key=lambda x: x[1][0])

    # for the graph
    y_id = []
    x1_startTime = []
    x2_runTime = []

    perIndx = 0
    contIndx = 0
    while perIndx < len(periods) and contIndx < len(contextList):
        per = periods[perIndx]
        contxt = contextList[contIndx]
        if (per[1][0] < contxt[0]):
            y_id.append(per[0])
            x1_startTime.append(per[1][0][0])
            x2_runTime.append(per[1][0][1] - per[1][0][0])
            perIndx += 1
        else:
            y_id.append(-1)
            x1_startTime.append(contxt[0])
            x2_runTime.append(contxt[1])
            contIndx += 1


    if perIndx < len(periods):
        for i in range(perIndx, len(periods)):
            per = periods[i]
            y_id.append(per[0])
            x1_startTime.append(per[1][0][0])
            x2_runTime.append(per[1][0][1] - per[1][0][0])

    return (y_id, x1_startTime, x2_runTime)

