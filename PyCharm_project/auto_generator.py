import numpy as np
import random
from process import *

#read data from an input file::
def read_input_file (file_name):
    f= open(file_name,"r")
    proc_num = int(f.readline())
    AT_parms,BT_parms,PR_parms= [[float(x) for x in line.split()] for line in f]
    return proc_num,AT_parms,BT_parms,PR_parms

#generate processes parameters to an output file::
def generate_processes(proc_num,AT_parms,BT_parms,PR_parms,file_name):
    #getting arrival times & burst times & periority 
    AT=abs(np.random.normal(AT_parms[0],AT_parms[1],proc_num))
    BT=abs(np.random.normal(BT_parms[0],BT_parms[1],proc_num))
    BT=BT+1
    PR=abs(np.random.poisson(PR_parms,proc_num))
    #writting the processes parameters in output file
    f=open(file_name,"a")
    f.write(str(proc_num)+"\n")
    for i in range (0,proc_num):
        f.write(str(i+1)+" "+str(int(AT[i]))+" "+str(int(BT[i]))+" "+str(int(PR[i]))+"\n")
    f.close()

#read the processes parameters from the previous output file
def read_proc_from_file(file_name):
    f= open(file_name,"r")
    processes = [] 
    f.readline()
    for line in f:
        arr= [int(x) for x in line.split()]
        pro= Process(arr[0],arr[1],arr[2],arr[3])
        processes.append(pro)
    return processes
    

#generate input file::
def generate_input_file(file_name,min_num=None,max_num=None):
    f=open(file_name,"a")
    if min_num is None or min_num <= 0:
        min_num=1
    if max_num is None or max_num < min_num:
        max_num= min_num+ 10
    min_num=int(min_num)
    max_num=int(max_num)
    
    n=random.randrange(min_num,max_num,1)
    f.write(str(n)+"\n")
    f.write(str(round(abs(random.random()),2))+" "+str(round(abs(random.random()),2))+"\n")
    f.write(str(round(abs(random.random()),2))+" "+str(round(abs(random.random()),2))+"\n")
    f.write(str(int(abs(random.random()))+5))
    f.close()
