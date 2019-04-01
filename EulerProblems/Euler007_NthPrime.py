from EulerProblems import primeHelpers
def runEuler007():
    n=10001
    primes=primeHelpers.populateWithSieve(1000000)
    print(primes[n-1])


