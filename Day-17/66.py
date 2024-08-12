# Write a menu driven program which has the following options:
# Prime or Not.
# Armstrong or Not.
# Perfect or Not.
# Palindrome or not.
# Exit.


import json


def prime(n):
    prime = True
    for i in range(2, n//2 + 1):
        if n % i == 0:
            prime = False
            break
    if prime == True :
        return "Prime"
    
def armstrong(n):
    sm = 0
    t = n
    while t > 0:
        dgt = t % 10
        sm += dgt ** 3
        t //= 10
    if n == sm:
        return "Armstrong"
    else:
        return "Not Armstrong"
    
def perfect(n):
    sm = 0
    for i in range(1, n):
        if n % i == 0:
            sm += i
    if sm == n:
        return "Perfect Number"
    else:
        return "Not Perfect Number"
    
def palindrome(n):
    rev = 0
    t = n
    while t > 0:
        dgt = t % 10
        rev = rev * 10 + dgt
        t //= 10
    if n == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
def lambda_handler(event, context):
    ch = event.get('ch')
    
    match ch:
        case 1:
            r = prime(event.get('n'))
        case 2:
            r = armstrong(event.get('n'))
        case 3:
            r = perfect(event.get('n'))
        case 4:
            r = palindrome(event.get('n'))
        case 5:
            return "EXIT.."
    
    return r
