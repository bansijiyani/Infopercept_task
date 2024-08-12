# Write a Python Program to Generate the following output.
# (a)
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# (b)
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
# (c)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# (d)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# (e)
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# (f)
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5
# (g)
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# (h)
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5
# (i)
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5
# (j)
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# (k)
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1
# 2 4 6 8 10
# 4 6 8 10
# 6 8 10
# 8 10
# 10
# (l)
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# (m)
# 1
# 0 1
# 0 1 0
# 1 0 1 0
# 1 0 1 0 1
# (n)
# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1
# (o)
# A B C D E F G F E D C B A 
# A B C D E F   F E D C B A 
# A B C D E	      E D C B A 
# A B C D		    D C B A 
# A B C			      C B A
# A B                   B A
# A	                      A



import json

def pattern(ch):
    
    result = []

    match ch:
        case 'a':
            for i in range(1, 6):
                result.append(" ".join(str(j) for j in range(1, 6)))
        case 'b':
            for i in range(1, 6):
                result.append(" ".join(str(i) for j in range(1, 6)))
        case 'c':
            for i in range(1, 6):
                result.append(" ".join(str(j) for j in range(1, i+1)))
        case 'd':
            for i in range(1, 6):
                result.append(" ".join(str(i) for j in range(1, i+1)))
        case 'e':
            for i in range(5, 0, -1):
                result.append(" ".join(str(i) for j in range(1, i+1)))
        case 'f':
            for i in range(5, 0, -1):
                result.append(" ".join(str(j) for j in range(5, i-1, -1)))
        case 'g':
            for i in range(1, 6):
                result.append(" ".join(str(j) for j in range(i, 0, -1)))
        case 'h':
            for i in range(5, 0, -1):
                result.append(" ".join(str(j) for j in range(i, 6)))
        case 'i':
            for i in range(1, 6):
                result.append(" ".join(str(j) for j in range(i, 6)))
        case 'j':
            for i in range(5, 0, -1):
                result.append(" ".join(str(j) for j in range(i, 0, -1)))
        case 'k':
            for i in range(5, 0, -1):
                result.append(" ".join(str(j*2) for j in range(6-i, 6)))
        case 'l':
            for i in range(1, 6):
                result.append(" ".join(str(j*2-1) for j in range(1, i+1)))
        case 'm':
            for i in range(1, 6):
                result.append(" ".join(str(j%2) for j in range(1, i+1)))
        case 'n':
            for i in range(1, 6):
                result.append(" ".join(str(j%2) for j in range(1, i+1)))
        case 'o':
            for i in range(1, 6):
                result.append(" ".join(str(j%2) for j in range(1, i+1)))
            

    return "\n".join(result)

def lambda_handler(event, context):
    ch = event.get('n', 'a')
    p = pattern(ch)
    
    return p


