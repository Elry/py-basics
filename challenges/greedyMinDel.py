from collections import Counter

def greed_del(A):
    cnt = Counter(A)

    freq = sorted(cnt.values(), reverse=True)
    print(freq)
    deletes = 0

    max_freq = freq[0] - 1

    for f in freq[1:]:
        print(f'current {f}')
        print(f'max: {max_freq}')
        if f > max_freq:
            if max_freq > 0:
                deletes += (f - max_freq)
            else:
                deletes += f

        max_freq = min(f, max_freq) - 1

    
    print(deletes)


A = 'aaabbbcc'
greed_del(A)
