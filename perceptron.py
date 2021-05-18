from textwrap import wrap
import re
import numpy as np

inputString = input ("Enter input-")

pattern = r'('
inputStringReplace = inputString.replace('(','')
inputStringReplace = inputStringReplace.replace(')','')
inputStringReplace = inputStringReplace.replace(',','')
inputStringReplace = inputStringReplace.replace(' ','')
functionType = inputStringReplace[0]
inputStringReplace = inputStringReplace.replace('P','')


inputStringWrapped = wrap(inputStringReplace,4)
inputAsArrayLen = len(inputStringWrapped)

print(inputStringReplace)
print(functionType)
print(inputStringWrapped)

maxIters = 100
completeLoop = False

#while (maxIters > 0 or completeLoop):


def needsWeightUpdated(inputVector, weightVector):
    xVector = []

    xVector.append(int(inputVector[0]) )
    xVector.append(int(inputVector[1]) )

    weightTimesXVectorVector = np.dot(xVector,weightVector)

    activation = 0
    for i in range (0,2,1):
        activation += weightTimesXVectorVector[i]
    
    returnVal = 0
    if activation > 0:
        returnVal = +1
    else:
        returnVal = -1
    return returnVal



#Do dot product between weightVector & inputVector 
#InputVector is a vector of the tuple -
# [x1
#  x2
#  y]

def updateWeights (inputVector, weightVector):
    xVector = []

    yVal = inputVector[2] + inputVector[3]
    yVal = int(yVal)

    xVector.append(int(inputVector[0]) )
    xVector.append(int(inputVector[1]) )
    
    xVector0TimesY =  xVector[0] * yVal
    xVector1TimesY =  xVector[1] * yVal

    weightVector[0] = weightVector[0] + (xVector0TimesY * yVal)
    weightVector[1] = weightVector[1] + (xVector1TimesY * yVal)





#def perceptron(inputVector):




