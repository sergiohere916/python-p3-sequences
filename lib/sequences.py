#!/usr/bin/env python3

def print_fibonacci(length):
    numbers = []
    for i in range(0, length):
        if (i < 2):
            numbers.append(i)
        else:
            numbers.append(numbers[i-1] + numbers[i-2])
        
    print(numbers)


(print_fibonacci(10))
