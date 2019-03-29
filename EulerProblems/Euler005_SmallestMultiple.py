from EulerProblems import primeHelpers
def runEuler005():
    limit=20
    primes=primeHelpers.populateWithSieve(1000000)
    primeFactorLists=map(lambda  n: primeHelpers.performPrimeFactorSearch(n,primes),range(1,limit+1))
    minSet={}
    for pfl in primeFactorLists:
        for prime in pfl.keys():
            if prime not in minSet or minSet[prime]<pfl[prime]:
                minSet[prime]=pfl[prime]
    retval=1
    for prime in minSet.keys():
        retval*=prime**minSet[prime]
    print(retval)