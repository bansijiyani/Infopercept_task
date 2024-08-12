# Write a program to print output as follow
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1


import json


def pattern():
    rs = []
    for i in range(1,6):
        row = []
        for j in range(1,6):
            if (i+j) % 2 == 0:
                row.append("1")
            else:
                row.append("0")
        rs.append(" ".join(row))
    return rs

def lambda_handler(event, context):
    return pattern()
