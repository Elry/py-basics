from concurrent.futures import ProcessPoolExecutor
import math

'''
bypass python GIL (Global Interpreter Lock), with separated process for each
best for RAG when chunking 1GB of text and local data processing
'''

def heavy_computation(n):
    return sum(math.sqrt(i) for i in range(n))

numbers = [10**6, 10**6, 10**6]


if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(heavy_computation, numbers))

    print("Done")
