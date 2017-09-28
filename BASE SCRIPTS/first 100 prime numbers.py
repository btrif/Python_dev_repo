prime_count = 1
start_number = 2
number_to_check = 2
while prime_count <= 100:
    result = number_to_check % start_number

    if result > 0:
        start_number += 1

    elif result == 0:
        if start_number == number_to_check:
            print (str(prime_count)+'.   \t' , number_to_check)
            number_to_check += 1
            prime_count += 1
            start_number = 2
        else:
            number_to_check += 1
            start_number = 2

input()
