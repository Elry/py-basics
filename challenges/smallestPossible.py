# Given an array A of N integers, return the smallest positive integer (greater than 0) that does not occur in A
def get_small(arrA):
    # set lookup is O(1)
    seen = set(arrA)
    print(seen)

    for i in range(1, len(arrA) + 2):
        if i not in seen:
            print(i)
            return i


def small_o_1(A):
    N = len(A)
    for i in range(N):
        while 1 <= A[i] <= N and A[A[i] - 1] != A[i]:
            print(A[i])
            correct_idx = A[i] - 1
            A[i], A[correct_idx] = A[correct_idx], A[i]

    for i in range(N):
        if A[i] != i+1:
            return i+1

    return N +1

arrA = [1, 3, 6, 4, 4, 1, 2]
# get_small(arrA)
print(small_o_1(arrA))
