#q1
from math import factorial

n = int(input ("Enter a value for n:"));
x=int (input("Enter the value for x:"));
def calEquation(n,x):
    sit =lambda n, k: n**k/ factorial(k)
    situ=[sit(n,k) for k in range (x+1)]
    total= sum(situ)+1

print("Result:", total )
#q2

n = int(input("Enter the number for terms: "))
def calSum(n):
    sum=0
    for k in range (1,n+1):
        sum += ((-1)**(k+1))/k

print("The result: ", sum)


