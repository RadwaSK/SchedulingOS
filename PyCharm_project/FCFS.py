from process import *

def FCFS(procs):
    processes = procs.copy()
    done = []
    step = 0
    processes.sort(key=lambda x: x.AT)

    while len(processes) > 0:
        p = processes[0]
        p.setStartTime(step)
        p.execute(step)
        processes.remove(p)
        done.append(p)
        step += p.BT

    done.sort(key=lambda x: x.AT)
    return done, []