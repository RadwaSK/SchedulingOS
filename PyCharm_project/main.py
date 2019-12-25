import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from auto_generator import *
from FCFS import *
from RR import *
from HPF import *
from SRTN import *
from output import *

print("Enter input file path: ")
file_path = input()
processes=read_proc_from_file(file_path)

print("write the scheduling algorithm name(RR,FCFS,HPF,SRTN): ")
algo = input()
if algo == "HPF":
    proc, contxtPeriods = HPF(processes)
elif algo == "FCFS":
    proc, contxtPeriods = FCFS(processes)
elif algo == "SRTN":
    print("Enter Context Switching Time: ")
    cntxt = input()
    proc, contxtPeriods = SRTN(processes, float(cntxt))
elif algo == "RR":
    print("Enter Context Switching Time: ")
    cntxt = input()
    print("Enter quantum: ")
    quantum = input()
    proc, contxtPeriods = RR(processes, int(quantum), float(cntxt))

# getting lists
x, y = getLists(proc, contxtPeriods)

plt.plot(x, y)
plt.ylabel("pid")
plt.xlabel("time steps")
plt.title(algo)
plt.grid()
plt.show()

# to be removed::
# for i in range (0,len(proc)):
#     print(proc[i].id, proc[i].startT, proc[i].finishT, proc[i].TAT)

