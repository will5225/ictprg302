#!/usr/bin/python3

import math
numbers = int(input("enter a number: "))

print (numbers)

for n in range(1, numbers + 1):
    print("the number is " +str(n) + " its square is " + str(int(math.pow(n,2))) + " and its cube is " + str(int(math.pow(n,3)))+ "")