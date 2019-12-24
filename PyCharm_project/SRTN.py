from process import *


def SRTN(processes, context_sw):
    proc = processes.copy()
    proc_num = len(proc)
    proc.sort(key=lambda x:x.AT)
    time = 0
    ready = []
    context = []
    i = 0
    last_processed = -1
    while 1:
        # enter process who arrived in the ready queue:
        while i < proc_num:
            if proc[i].AT > time:
                break
            ready.append([proc[i].remainingT, i])
            i += 1
        # sort the ready queue according to remaining time:
        ready.sort()
        
        if len(ready) == 0 and i < proc_num:
            time = proc[i].AT
        elif i >= proc_num and len(ready) == 0:
            break
        
        # execute the current process with stander quantum=1:
        if len(ready) > 0:
            p = ready[0]
            # if last process didn't finish or next one will be loaded --> context switching:
            if (last_processed != -1 and p[1] != last_processed)and (proc[p[1]].startT != -1
                                                                     or proc[last_processed].finishT == -1):
                context.append([time, time+context_sw])
                time += context_sw
            if proc[p[1]].remainingT == proc[p[1]].BT:
                proc[p[1]].setStartTime(time)
            rem_time = proc[p[1]].execute(time, 1)
            time = time + 1.0
            last_processed = p[1]   # id of processed process
            if rem_time == 0:
                ready.remove(p)
    proc.sort(key=lambda x: x.id)
    return proc, context
