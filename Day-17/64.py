# Write a menu driven program which has the following options:
# Positive or Negative.
# Even or Odd.
# Leap Year or Not Leap Year.
# Maximum of two numbers.
# Exit.
# Make use of SWITCH statement.

import json

def pos_neg(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap year"
            else:
                return "Not a leap year"
        else:
            return "Leap year"
    else:
        return "Not a leap year"


def max_num(num1, num2):
    return max(num1, num2)   


def lambda_handler(event, context):
    choice = event.get('choice')
    
    match choice:
        case 1:
            r = pos_neg(event.get('num'))
        case 2:
            r = even_odd(event.get('num'))
        case 3:
            r = leap_year(event.get('year'))
        case 4:
            r = max_num(event.get('num1'), event.get('num2'))
        case 5:
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "result": "EXIT.."
                })
            }
        case _:
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "result": "Invalid choice"
                })
            }
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": r
        })
    }