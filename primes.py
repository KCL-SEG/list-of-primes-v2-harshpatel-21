"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be positive")
    
    primes_list = []
    count = 0
    i=2
    while count<number_of_primes:
        if is_prime(i):
            primes_list += [i]
            count+=1
        i+=1
    return primes_list
        
def is_prime(n):
    return all(n%i for i in range(2,int((n**0.5)+1)))


print(primes(10))