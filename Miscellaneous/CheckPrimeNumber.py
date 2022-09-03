def check_prime_number(n):
    is_prime = False
    for i in range(2,n):
        if n%i == 0:
            is_prime = True
    if is_prime:
        print('Not a prime number')
    else:
        print('Prime number')

n = int(input())
check_prime_number(n)