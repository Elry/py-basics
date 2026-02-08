from collections import Counter
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numLen = len(nums)
        counts = Counter(nums)

        for index, item in enumerate(nums):
            print(nums[index])
        duplicates = [num for num, count in counts.items() if count > 2]
        print(duplicates)


solution = Solution()
solution.removeDuplicates([1, 1, 2, 3, 3, 3])