# Write a program to generate following output
# 1
# 4 5
# 9 10 11
# 16 17 18 19
# 25 26 27 28 29
# .
# .

import json

def p(n):
    rs = []
    c = 1
    for i in range(1, n+1):
        rs.append(i.join(" "))

def lambda_handler(event, context):
    return p(5) 