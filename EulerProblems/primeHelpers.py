import itertools
def populateWithSieve(maxNeededPrime):

    prime=[True for i in range(maxNeededPrime+1)]
    p = 2
    while ((p-2) * (p-2) <= maxNeededPrime):
        if prime[p]:
            for i in range(p * 2, maxNeededPrime + 1, p):
                prime[i] = False
        p += 1
    retval=list(filter(lambda n:prime[n],range(2,maxNeededPrime)))
    return retval
def performPrimeFactorSearch(target,primeList):
    retval={}
    findPrimeFactors(target,retval,primeList,2)
    return retval
def findPrimeFactors(target,primeFactors,primeList,n):
    if target==1 :
        return
    for cursor in itertools.count(n,1):
        factorCandidate=primeList[cursor]
        if target % factorCandidate==0:
            if factorCandidate not in primeFactors:
                primeFactors[factorCandidate]=0
            primeFactors[factorCandidate]+=1
            findPrimeFactors(target/factorCandidate,primeFactors,primeList,cursor)
            break
        else:

            if factorCandidate * factorCandidate >= target:
                primeFactors[int(target)] = 1
                break

