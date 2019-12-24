from auto_generator import *

print("Enter name for the file:")
data_file_name= input()

generate_input_file("in"+data_file_name)

proc_num,AT_parms,BT_parms,PR_parms=read_input_file("in"+data_file_name)

generate_processes(proc_num,AT_parms,BT_parms,PR_parms,data_file_name)
