#!usr/bin/env python3
def sui():
    b1 = int(input("input a number"))
    binary = bin(b1)
    print(binary[2:])
    quit()
    return sui()

def find_factors(n):
    factorlist = []
    for i in range(1,n+1):
        if (n%i == 0):
            factorlist.append(i)
            print(factorlist)
    return(factorlist)

def primenum(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
