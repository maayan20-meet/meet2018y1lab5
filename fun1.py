def add_numbers(start, end, n):
    
    SUM = 0
    for number in range(start, end + 1):
        SUM = number + SUM  
    return SUM

answer = add_numbers(1,100, 1)
print(answer)
test2 = add_numbers(333,777, 1)
print(test2)
test3 = add_numbers(1, 10, 2)
print(test3)

