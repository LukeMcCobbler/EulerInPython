import math
def runEuler003():
    maxNeededPrime=int(math.sqrt(600851475143))
    primes=populateWithSieve(maxNeededPrime)
def populateWithSieve(maxNeededPrime):
    math.sqrt(maxNeededPrime)
    prime=[True for i in range(maxNeededPrime+1)]
    p = 2
    while (p * p <= maxNeededPrime):
        if prime[p]:
            for i in range(p * 2, maxNeededPrime + 1, p):
                prime[i] = False
        p += 1
    retval=set(filter(lambda n:prime[n],range(maxNeededPrime)))
    return retval;

