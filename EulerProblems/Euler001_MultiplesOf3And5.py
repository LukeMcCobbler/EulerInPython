import math
def multiplesOfXUnderN(x,n):
    multCount=math.floor((n-1)/x)
    multSum=((multCount+1)*multCount)/2*x
    return multSum
def solveEuler001():
    multsOf3Under100=multiplesOfXUnderN(3,1000)
    multsOf5Under100=multiplesOfXUnderN(5,1000)
    multsOf15Under100=multiplesOfXUnderN(15,1000)
    retval=multsOf3Under100+multsOf5Under100-multsOf15Under100
    return retval
def runEuler001():
    print(solveEuler001())
