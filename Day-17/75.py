# Write a program to count the vowels and letters in text given as standard input. Then print out the number of occurrences of each of the vowels a, e, i, o and u in the text, the total number of letters, and each of the vowels as an integer percentage of the letter total.

# Suggested output format is:

# Numbers of characters:
# a	3 ; e	2 ; i	0 ; o	1 ; u	0 ; rest 17 Percentages of total:
# a 13%; e  8%; i  0%; o  4%; u  0%; rest 73%



def count_vowels(txt):
    vowels = "aeiouAEIOU"
    v_cnt = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    letter = 0

    for char in txt:
        if char.isalpha():
            letter += 1
            if char.lower() in vowels:
                v_cnt[char.lower()] += 1

    return v_cnt, letter

def lambda_handler(event, context):
    txt = event.get('txt')

    if txt is None:
        return "Please enter valid txt.."

    v_cnt, letter = count_vowels(txt)
    rs = ""

    for v in "aeiou":
        rs += v + "\t" + str(v_cnt[v]) + " ; "

    rest = letter - sum(v_cnt.values())
    rs += "rest " + str(rest)

    rs += "Percentages of total:"
    for v in "aeiou":
        percentage = int(v_cnt[v] / letter * 100)
        rs += v + " " + str(percentage) + "%; "

    return rs
