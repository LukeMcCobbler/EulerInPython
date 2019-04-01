def runEuler006():
    numberOfNaturalNumbers=100
    sumDifferences=map(lambda n:n**3-n**2,range(1,numberOfNaturalNumbers+1))
    print(sum(sumDifferences))