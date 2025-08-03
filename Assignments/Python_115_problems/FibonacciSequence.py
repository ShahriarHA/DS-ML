# 24. Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.

n = int(input())
fibonacciSeq = [0,1]
for i in range(2,n):
    fibonacciSeq.append(fibonacciSeq[i-2]+fibonacciSeq[i-1])
print(fibonacciSeq)



