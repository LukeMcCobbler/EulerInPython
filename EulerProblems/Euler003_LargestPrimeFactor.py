import math
import itertools
def runEuler003():
    target=600851475143
    maxNeededPrime=int(math.sqrt(target))
    primes=populateWithSieve(1000000)
    primeFactors={}
    findPrimeFactors(target,primeFactors,primes,2)
    print(primeFactors)
def findPrimeFactors(target,primeFactors,primeList,n):
    if target==1 :
        return
    for cursor in itertools.count(n,1):
        factorCandidate=primeList[cursor]
        print("Testing divisibility of %d with %d"%(target,factorCandidate))
        if target % factorCandidate==0:
            print("Yes!")
            if factorCandidate not in primeFactors:
                primeFactors[factorCandidate]=0
            primeFactors[factorCandidate]+=1
            findPrimeFactors(target/factorCandidate,primeFactors,primeList,cursor)
            break
        else:
            print("No :-(")
            if factorCandidate * factorCandidate >= target:
                primeFactors[int(target)] = 1
                break
def populateWithSieve(maxNeededPrime):
    print("Calculating sieve for primes up to %d" % maxNeededPrime)
    prime=[True for i in range(maxNeededPrime+1)]
    p = 2
    while ((p-2) * (p-2) <= maxNeededPrime):
        if prime[p]:
            for i in range(p * 2, maxNeededPrime + 1, p):
                prime[i] = False
        p += 1
    retval=list(filter(lambda n:prime[n],range(maxNeededPrime)))
    return retval

