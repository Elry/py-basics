from math import factorial
import matplotlib.pyplot as plt

def fibonacci(sequence_length):
    "Return the Fibonacci sequence of length *sequence_length*"
    sequence = [0,1]
    if sequence_length < 1:
        print("Fibonacci sequence only defined for length 1 or greater")
        return
    if 0 < sequence_length < 3:
        return sequence[:sequence_length]
    for i in range(2,sequence_length): 
        sequence.append(sequence[i-1]+sequence[i-2])
    return sequence

fibs = fibonacci(10)
facts = []

for i in range(10):
  facts.append(factorial(i))

plt.semilogy(facts,label="Factorial")
plt.semilogy(fibs,label="Fibonacci")
plt.xlabel("n")
plt.legend()

plt.show()
