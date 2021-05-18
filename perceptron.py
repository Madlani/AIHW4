from textwrap import wrap
import re


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
