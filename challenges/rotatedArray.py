'''
Find the minimum element in a sorted array that has been rotated.Constraint: 
  You must do this in $O(\log N)$ time. (No min(), no loops).
  Example:Original: [0, 1, 2, 4, 5, 6, 7] (Min is 0).
  Rotated: [4, 5, 6, 7, 0, 1, 2] (Min is 0).
'''

def finder(nums):
    if not nums: return 0
    if len(nums) == 1: return nums[0]

    left = 0
    right = len(nums) - 1

    if nums[left] < nums[right]:
        return nums[left]

    while left < right:
        mid = (left+right) // 2

        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid

    print(nums[left])


finder([4, 5, 6, 7, 0, 1, 2])
