memo = {}

def climb_stairs(n):
    if n <= 1: return 1

    if n in memo:
        return memo[n]
    
    # 3. Recurrence Relation
    # Ways(n) = Ways(n-1) + Ways(n-2)
    result = climb_stairs(n-1) + climb_stairs(n-2)
    
    # 4. Save to Cache
    memo[n] = result
    return result

print(climb_stairs(5))  # Output: 8
# Without 'memo', this would be O(2^n). With 'memo', it is O(n).
