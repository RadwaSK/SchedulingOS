import numpy as np

# valid assumption: the new arrived processes are inserted in the beginning of the queue
# and any processed process is removed from queue and inserted in the back

def RR(processes, quantum, contextSwitchingTime):
    step = 0
    last_processed = 1
    queue = []
    while len(processes) > 0 or len(queue) > 0:
        # add arrived processes to the queue
        tempQ = queue
        queue = []
        for p in processes:
            if p[1] <= step:
                queue.append(p)
                processes.remove(p)

        queue += tempQ

        # print("At time step ", step, "queue has ", queue)
        # print("At time step ", step, "processes has ", processes)

        if len(queue) > 0:
            p = queue[0]
            queue.remove(p)
            # print("processing process number ", p[0])
            p[2] -= quantum
            p[2] = max(p[2], 0)
            # print("Now it has burst time = ", p[2])
            if p[2] != 0:
                queue.append(p)
            # else:
                # print("process ", p, " is finished")

            step += quantum
            # print("now time is ", step)
            if p[0] != last_processed and (len(processes) > 0 or len(queue) > 0):
                step += contextSwitchingTime
                # print("adding context switching time, so step now is ", step)
            last_processed = p[0]
        # print("")
        # print("")

# processes = [[1, 0, 3],
#              [2, 1, 5],
#              [3, 3, 2],
#              [4, 9, 5],
#              [5, 12, 5]]
#
# RR(processes, 3, 1)