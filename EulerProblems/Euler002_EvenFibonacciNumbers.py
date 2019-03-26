import sys
import math
import itertools
def getFib(n,memo):
    if(n<2):
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            retval=getFib(n-1,memo)+getFib(n-2,memo)
            memo[n]=retval
            return retval
def allFibs(memo):
    return map(lambda n:getFib(n,memo),range(1, sys.maxsize))
def evenElementsUnderX(iterable,x):
    return filter(lambda n:n%2==0, itertools.takewhile(lambda c:c<x,iterable))
def runEuler002():
    memo={}
    evenFibsUnderAMillion=sum(evenElementsUnderX(allFibs(memo),4000000))
    print(evenFibsUnderAMillion)