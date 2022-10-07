"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()

def isEven(numbers):
    if len(numbers)%2==0:
        evenList(numbers)
    else:
        oddList(numbers)
def evenList(numbers):
    half=int(len(numbers)/2)
    to_mean=(numbers[half-1],numbers[half])
    mean(to_mean)

def mean(tup):
    print (sum(tup)/2)

def oddList(numbers):
    print(numbers[len(numbers)//2])

isEven(numbers)
