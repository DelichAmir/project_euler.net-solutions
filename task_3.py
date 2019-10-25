
n = 600851475143
def Largest_Prime_Factor(number):
    '''
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    '''
    x = 2
    prime_factors = []
    while x * x <= number:
        while number % x == 0:
            prime_factors.append(x)
            number /= x
            number = int(number)
        x += 1
    if number > 1:
        prime_factors.append(number)

    return prime_factors[-1]

print(f'The largest prime factor of the number {n}: ' ,Largest_Prime_Factor(n))