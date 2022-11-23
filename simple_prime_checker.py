#from random import randint
import random

def random_number():
    return random.randint(1,100000)

def is_prime(a):
    '''
    Return a list of the factors of a. If the number has no factors, tells me if it is a prime number
    '''
    factors = []
    
    for num in range(2,a): 
        if a % num == 0:
            factors.append(num)
        else:
            pass
    
    print(f'Your randomly chosen number is: {a}')
    
    if len(factors) > 0:
        print(f'This number is NOT prime and divisible by this list of ATTRACTIVE numbers: {factors}')
    else:
        print(f'This number is prime.')
        print(f'This means your number is only divisible by 1 and itself {a}')

#Randomly chooses a number between 1 and 100 thousand
#Is number prime or composite. If composite, lists factors. If prime, explains is a prime number

number = random_number()
is_prime(number)