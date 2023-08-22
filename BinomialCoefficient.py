import math
n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
#nFact=math.factorial(n)
#rFact=math.factorial(r)
#nMrFact=math.factorial(n-r)
nCr=math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
#nCr=nFact/(rFact*nMrFact)
print("The value of nCr is : ", nCr)
