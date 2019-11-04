prime_numbers = [2]

# N -index of prime number
def Is_Prime(N):
    '''
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    '''

    for n in range(3, 110_000):
        if len(prime_numbers) < N:
            for k in prime_numbers:
                if (n % 2 == 0) or (n % k == 0):
                    break
            else:
                prime_numbers.append(n)
        else:
            break

Is_Prime(10_001)

print(f"Prime numbers: {prime_numbers}")
print(f"Max index: {len(prime_numbers)}")
print(f"Result: {prime_numbers[-1]}")