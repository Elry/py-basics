# The Key Question:To do this efficiently, we need a way to instantly check
# "Have I seen this character before in my current window?
# "What Python data structure gives us $O(1)$ (instant) lookups to check for existence?
# (Is it a List, a Set, or a Tuple?)
# The Problem: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
def length_of_longest_substring(s):
    seen = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # 1. THE WHILE LOOP:
        # As long as s[right] is ALREADY in 'seen', 
        # remove s[left] from 'seen' and move left forward.
        while s[right] in seen:
            seen.discard(s[left])
            left += 1
        
        # 2. Add s[right] to 'seen'
        seen.add(s[right])
        
        # 3. Update max_len (Current window size is: right - left + 1)
        max_len = max(max_len, right - left + 1)
        
    print(max_len)
    print(seen)

length_of_longest_substring('abcabcbb')