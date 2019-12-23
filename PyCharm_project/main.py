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
    proc = HPF(processes)
elif algo == "FCFS":
    proc = FCFS(processes)
elif algo == "SRTN":
    print("Enter Context Switching Time: ")
    cntxt= input()
    proc = SRTN(processes, float(cntxt))
elif algo == "RR":
    print("Enter Context Switching Time: ")
    cntxt= input()
    print("Enter quantum: ")
    quantum= input()
    proc = RR (processes, int(quantum), float(cntxt))
    
# to be removed::
for i in range (0,len(per)):
    print(per[i].id,per[i].startT,per[i].finishT,per[i].TAT)