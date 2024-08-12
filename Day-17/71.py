# Display the following triangle up to given lines.
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *

import json

def ptrn(n):
    rs = []
    for i in range(1, n+1):
        rs.append(" * "* i )
    return rs

def lambda_handler(event, context):
    return ptrn(5)


