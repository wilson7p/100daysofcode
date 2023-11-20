#Write a program to print the first 10 prime numbers. 
print ("\nWilson - Day 4 of #100DaysOfCode\n")
print("\nprint the first 10 prime numbers\n")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(count):
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Print the first 10 prime numbers
first_10_primes = generate_primes(10)
print("The first 10 prime numbers are:", first_10_primes)
