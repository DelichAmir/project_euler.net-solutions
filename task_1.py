

numbers = range(1, 1000)
mul_num_1 = 3
mul_num_2 = 5

def sum_of_all_multiples(num, n1, n2, *, result = 0):
    '''
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    '''

    for l in num:
        if l%n1 == 0 or l%n2 == 0:
            result += l
    return result

print(f"Sum of all the multiples of {mul_num_1} or {mul_num_2} below {numbers}: ", sum_of_all_multiples(numbers,3,5))


