# Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.
# Hint: Calculate the sum of the first k elements first, then loop from k to the end of the list.
def max_subarray_sum(nums, k):
    current_sum = sum(nums[:k])
    final_sum = current_sum

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i-k]
        final_sum = max(final_sum, current_sum)
    print(final_sum)
max_subarray_sum([1,2,3], 3)
