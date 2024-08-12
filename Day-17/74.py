# Write a Python Program to print the following series
# A B C D E
# F G H I
# J K L
# M N
# O

import json

def p():
    rs = []
    c = 65
    for i in range(5, 0, -1):
        rs.append(" ".join(chr(j) for j in range(c, c+i)))
        c += i
    return rs

def lambda_handler(event, context):
    return p()
