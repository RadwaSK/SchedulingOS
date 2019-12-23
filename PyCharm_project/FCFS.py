from process import *

def FCFS(procs, contextSwitchingTime):
    processes = procs.copy()
    step = 0
    processes.sort(key=lambda x: x.AT)

    while len(processes) > 0:
        p = processes[0]
        p.setStartTime(step)
        p.execute(step)
        processes.remove(p)
        step += p.BT
        if len(processes) > 0:
            step += contextSwitchingTime

