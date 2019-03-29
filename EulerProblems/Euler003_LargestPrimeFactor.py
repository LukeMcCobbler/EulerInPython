import math
from EulerProblems import primeHelpers
import itertools
def runEuler003():
    target=600851475143
    maxNeededPrime=int(math.sqrt(target))
    primes=primeHelpers.populateWithSieve(1000000)
    primeFactors={}
    primeHelpers.findPrimeFactors(target,primeFactors,primes,2)
    print(max(primeFactors))
