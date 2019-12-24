from process import *

# valid assumption: the new arrived processes are inserted in the beginning of the queue
# and any processed process is removed from queue and inserted in the back

def RR(procs, quantum, contextSwitchingTime):
    processes = procs.copy()
    done = []
    step = 0
    last_processed = 1
    queue = []
    while len(processes) > 0 or len(queue) > 0:
        # add arrived processes to the queue
        tempQ = queue
        queue = []
        for p in processes:
            if p.AT <= step:
                p.setStartTime(step)
                queue.append(p)
                processes.remove(p)

        queue += tempQ

        # print("At time step ", step, "queue has ", queue)
        # print("At time step ", step, "processes has ", processes)

        if len(queue) > 0:
            p = queue[0]
            queue.remove(p)
            if p.id != last_processed and (len(processes) > 0 or len(queue) > 0):
                step += contextSwitchingTime
                # print("adding context switching time, so step now is ", step)

            # print("processing process number ", p[0])
            stat = p.execute(step, quantum)

            step += quantum

            if stat != 0:  # not finished yet
                queue.append(p)
            else:
                done.append(p)

            last_processed = p.id
        # print("")
        # print("")
    done.sort(key=lambda x: x.AT)
    return done


p1 = Process(1, 0, 3, 1)
p2 = Process(2, 1, 5, 2)
p3 = Process(3, 3, 2, 3)
p4 = Process(4, 9, 5, 4)
p5 = Process(5, 12, 5, 5)
processes = [p1, p2, p3, p4, p5]
RR(processes, 1, 0)
#print(step)
