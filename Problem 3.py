def is_prime(x, div=2):
    if x % div == 0:
        return False
    elif div >= x / 2:
        return True
    else:
        return is_prime(x, div + 1)

# divide by x/2
# and keep going down
# then repeat for each of the values
# until smallest primes are reached
# then print the list out
def prime_factors(x):
    
