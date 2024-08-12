# Write a Python Program to print the output as follows. 
# C
# CP
# CPr
# CPro 
# CProg 
# CProgr 
# CProgra 
# CProgram
# CProgramm 
# CProgrammi 
# CProgrammin 
# CProgramming

import json

def pattern():
    s = "CProgramming"
    l = len(s)
    result = []
    for i in range(l):
        result.append(s[:i+1])
    return result

def lambda_handler(event, context):
    p = pattern()
    # print(p)
    return p

