from process import *


def HPF(processes):
    proc = processes.copy()
    proc_num = len(proc)
    proc.sort(key=lambda x: x.AT)
    time = 0
    ready = []
    i = 0
    while 1:
        # enter process who arrived in the ready queue:
        while i < proc_num:
            if proc[i].AT > time:
                break
            ready.append([-proc[i].P, i])
            i += 1
        # sort the ready queue according to processes' priority:
        ready.sort()
        
        if len(ready) == 0 and i < proc_num:
            time = proc[i].AT
        elif i >= proc_num and len(ready) == 0:
            break
        
        # execute the highest priority process:
        if len(ready) > 0:
            p = ready[0]
            proc[p[1]].setStartTime(time)
            proc[p[1]].execute(time)
            ready.remove(p)
            time += proc[p[1]].BT
        
    proc.sort(key=lambda x: x.id)
    return proc, []
