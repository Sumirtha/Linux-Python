from prime import Prime

def printPrimes(n):
    count = 0
    num = 2
    while count < n:
        if isPrime(num):
            print(num, end=" ")
            count += 1
        num += 1
    print()
printPrimes(10)