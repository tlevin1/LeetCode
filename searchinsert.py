'''
35. Search Insert Position


Given a sorted array of distinct integers and a target value, return the index if the target is found.If
not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1, 3, 5, 6], target = 5
Output: 2

Example 2:

Input: nums = [1, 3, 5, 6], target = 2
Output: 1

Example 3:

Input: nums = [1, 3, 5, 6], target = 7
Output: 4

Example 4:

Input: nums = [1, 3, 5, 6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104 nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #approach: binary search on array check if target is greater than
        # left of mid or right of mid and check left or right. if not found then returns final left val
        n = len(nums) - 1
        l,r = 0, n
        #insert at begnining check
        if target < nums[0]:
            return 0
        #insert at end
        if target > nums[n]:
            #nums.append(target)
            return n + 1

        while l < r:
            mid = int((l + r) / 2)
            if target == nums[mid]:
                #found target in arr
                return mid
            #check right
            if target > nums[mid]:
                l = mid + 1
            #check left
            if target < nums[mid]:
                r = mid
        #once left > r found place to insert
        return l

    def main(self):
        print(self.searchInsert([1,3,5,7],6))

obj = Solution()
obj.main()