# Write a Python Program to print the out as follows 
# PyProgrammin 
# PyProgrammi 
# PyProgramm 
# PyProgram 
# PyProgra 
# PyProgr 
# PyProg
# PyPr

import json

def pattern():
    s = "py Programming"
    l = len(s)
    rs = []
    for i in range(l,0,-1):
        rs.append(s[:i])
    return rs

def lambda_handler(event, context):
    p = pattern()
    # print(p)
    return p
