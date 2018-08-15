number = 2
prime_numbers = [1]
list_prime = 0

while number <= 1000:
    while list_prime <= len(prime_numbers):
        if number / prime_numbers[list_prime] == int:
            prime_numbers.append(number)
            number += 1
        else:
            number += 1

print(prime_numbers)
   


    
    
