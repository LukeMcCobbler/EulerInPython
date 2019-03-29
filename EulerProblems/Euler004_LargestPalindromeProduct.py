import itertools
def runEuler004():
    digitCount=3
    factors=numbersWithNDigits(digitCount)
    factors.sort(reverse=True)
    maxCandidate=factors[0]*factors[0]
    candidates=map(lambda x:maxCandidate-x, itertools.takewhile(lambda y:y<=maxCandidate,itertools.count()))
    firstMatch=next(filter(lambda x:isPalindromic(x) and isProductOfTwoNDigits(x,factors,digitCount) ,candidates))
    print(firstMatch)
    return
def isProductOfTwoNDigits(number,factorList,digitCount):
    retval=any(filter(lambda x: number%x==0 and hasNDigits(number/x,digitCount),  factorList))
    return retval
def hasNDigits(n,digitcount):
    retval=(n>=10**(digitcount-1) and n<10**digitcount)
    return retval
def isPalindromic(n):
    strRep=str(n)
    strLen=len(strRep)
    charsToCompare=int((strLen-(strLen%2))/2)
    retval=all(map(lambda i: strRep[i]==strRep[strLen-i-1] ,range(charsToCompare)))
    return retval
def numbersWithNDigits(n):
    min=10**(n-1);
    max=10**(n)-1
    retval=list( itertools.takewhile(lambda x:x<=max, itertools.count(min)))
    return retval