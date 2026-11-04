for n in range(1,1001):
    if n % 15 == 0:
        print(f'{n}: FIZZBUZZ')
    elif n % 5 == 0:
        print(f'{n}: FIZZ')
    elif n % 3 == 0:
        print(f'{n}: BUZZ')
    else: 
        print(n)
