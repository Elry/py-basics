class Solution:
    def merge(nums1, m: int, nums2, n: int) -> None:
        p1 = m - 1 
        p2 = n - 1
        p = m + n - 1

        # While there are elements to be merged
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are still elements in nums2, copy them over
        # (If there are remaining elements in nums1, they are already in place)
        nums1[:p2 + 1] = nums2[:p2 + 1]
        print(nums1)
    
sol = Solution
sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)