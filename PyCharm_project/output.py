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
    lastX = 0
    while perIndx < len(periods) and contIndx < len(contextList):
        per = periods[perIndx]
        contxt = contextList[contIndx]
        if per[1][0][0] <= contxt[0]:
            if per[1][0][0] != lastX:
                y_id.append(0)
                x1_startTime.append(lastX)
                x2_runTime.append(per[1][0][0])

            y_id.append(per[0])
            x1_startTime.append(per[1][0][0])
            x2_runTime.append(per[1][0][1] - per[1][0][0])
            lastX = per[1][0][1]
            perIndx += 1
        else:
            if contxt[0] != lastX:
                y_id.append(0)
                x1_startTime.append(lastX)
                x2_runTime.append(contxt[0])

            y_id.append(-1)
            x1_startTime.append(contxt[0])
            x2_runTime.append(contxt[1])
            lastX = contxt[1]+contxt[0]
            contIndx += 1


    if perIndx < len(periods):
        for i in range(perIndx, len(periods)):
            per = periods[i]
            y_id.append(per[0])
            x1_startTime.append(per[1][0][0])
            x2_runTime.append(per[1][0][1] - per[1][0][0])

    yPts = [0]
    xPts = [0]

    for i in range(0, len(y_id)):
        x1, x2, y = x1_startTime[i], x2_runTime[i], y_id[i]
        yPts.append(y)
        yPts.append(y)
        xPts.append(x1)
        xPts.append(x1 + x2)

    xPts.append(xPts[-1])
    yPts.append(0)

    return xPts, yPts

