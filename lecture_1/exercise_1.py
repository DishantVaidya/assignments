# This program returns number of prime numbers up to a given number by user input..

try:
    n = int(input("Enter how many prime numbers you want: "))
    if n <= 0:
        print("Enter a positive number please.")
    else:
        primes = []
        num = 2

        while len(primes) < n:
            # Assume num is prime
            prime = True
            for i in range(2, num):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                primes.append(num)
            num += 1

        print("Primes:", primes)
except:
    print("Please enter a valid integer.")
