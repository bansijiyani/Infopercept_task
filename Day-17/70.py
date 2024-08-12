# (p)
# 1
# 232
# 34543
# 4567654
# 567898765
# 67890109876
# 7890123210987
# 890123454321098
# 90123456765432109
# 0123456789876543210

import json

def pattern():
    s = "0123456789"
    l = len(s)
    rs = []
    for i in range(1, l+1):
        rs.append(" ".join(str(j) for j in range(i, 0, -1)))
    return rs



def lambda_handler(event, context):
    p = pattern()
    return p