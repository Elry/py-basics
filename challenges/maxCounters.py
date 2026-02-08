def max_counters(arr, N):
    counters = [0] * N
    
    current_max = 0      # Tracks the highest value seen so far
    last_max_update = 0  # The "baseline" value from the last Max Counter command

    for a in arr:
        if a == N + 1:
            # Lazy update: Just record the baseline. Don't touch the array!
            last_max_update = current_max
        else:
            # It's a normal increment for counter at index `idx`
            idx = a - 1 
            
            # 1. Sync this counter if it's behind the baseline
            if counters[idx] < last_max_update:
                counters[idx] = last_max_update
            
            # 2. Increment
            counters[idx] += 1
            
            # 3. Update current_max if we just beat the record
            if counters[idx] > current_max:
                current_max = counters[idx]

    # Final Sweep:
    # Any counter we didn't touch since the last "Max Counter" command 
    # might still be old. Update them now.
    for i in range(N):
        if counters[i] < last_max_update:
            counters[i] = last_max_update
            
    return counters

arrA = [3, 4, 4, 6, 1, 4, 4]
print(max_counters(arrA, 5))

