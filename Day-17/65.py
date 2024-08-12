# Write a menu driven program which has the following options:
# Factorial of a number.
# Reverse of a number.
# Sum of Digits of a number.
# Count Digits of a number.
# Exit.

import json


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
def reverse(num):
    return int(str(num)[::-1])

def sum_of_digits(num):
    sm = 0

    while num > 0:
        sm += num % 10
        num //= 10
    return sm

def count_digits(num):
    cnt = 0

    while num > 0:
        cnt += 1
        num //= 10 
    return cnt

def lambda_handler(event, context):
    ch = event.get('ch')
    n = event.get('n')

    match ch:
        case 1:
            r = factorial(n)
            rs = "Factorial is " , r
        case 2:
            r = reverse(n)
            rs = "Reverse is " , r
        case 3:
            r = sum_of_digits(n)
            rs = "Sum of Digits is " , r
        case 4:
            r = count_digits(n)
            rs = "Count of Digits is " , r
        case 5:
            return "EXIT.."
        
    return rs
            