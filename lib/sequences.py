#!/usr/bin/env python3
def print_fibonacci(length):
    if length == 0:
        print("The Fibonacci sequence of length 0 is an empty list.")
        return

    first = 0
    second = 1
    print(first, end=" ")

    if length >= 2:
        print(second, end=" ")
        length -= 2
    else:
        return

    while length > 0:
        print(first + second, end=" ")
        temp = second
        second = first + second
        first = temp
        length -= 1

print_fibonacci(8)
