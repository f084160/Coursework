#Recall that a prime number is an integer greater than 1 that is divisible only by itself and 1.
#The prime numbers start with 2, 3, 5, 7, 11, 13, 17, . . .
#The flow chart below describes a method to find all prime numbers less than or equal to a given limit n.
#Implement the method as a Python function called findPrimes.
#The function should take one integer argument (the limit n)
#and return a list of integers which are the primes up to n.



def findPrimes(n):
    """This function takes one input integer argument n and returnd a list of integers which are the prime numbers up to n"""
    if n <= 1:
        raise ValueError ("The input you have entered is not a prime number, a prime number is an interger that is didvisable only by itself and 1")
    knownPrimes = []
    possibilities = list(range(2,n+1))
    while possibilities !=[]:
        p = possibilities[0]
        knownPrimes.append(p)
        x =len(possibilities)
        for i in range(x-1,-1,-1):
            if possibilities[i]%p == 0:
                del possibilities[i]
    return knownPrimes


        
                          
        
    
