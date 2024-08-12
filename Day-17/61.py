def count_odd_even_digits(number):
    odd_count = 0
    even_count = 0
    for digit in str(number):
        if digit.isdigit(): 
            if int(digit) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return {"odd": odd_count, "even": even_count}

if __name__ == "__main__":
    number = input("Enter a number: ")
    result = count_odd_even_digits(number)
    print(f"Odd digits: {result['odd']}, Even digits: {result['even']}")
