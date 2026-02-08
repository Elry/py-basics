# The Problem: Given a sorted array of integers, find two numbers that add up to a specific target.
# Example: nums = [2, 7, 11, 15] target = 9
def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if (current_sum == target):
            print(left, right)
            return
        elif current_sum > target:
            right -= 1
        else:
            left += 1


two_sum([1,2,3,4,5,6], 10)