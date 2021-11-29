'''Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums.If target exists, then
return its index.Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''
from bisect import bisect_left, bisect
from typing import List


class Solution(object):
    #Approach: binary search, repeatedly divide search interval into half

    def search(self, nums: List[int], target: int) -> int:
        # bisect_left() returns the first occurrence of the element to be found.If
        # there is none, it will return the index of where to insert our value
        # to keep  an ascending order.
        # bisect() will  return the index of where to insert our value to keep an
        # ascending order.
        print(bisect_left(nums, target))
        print(bisect(nums, target))

        if bisect_left(nums, target) != bisect(nums, target):
            return nums.index(target)
        else:
            return -1


    def main(self):
        print(self.search([1,2,3],3))
        print(self.search([-1, 0, 3, 5, 9, 12],9))
        print(self.search([5], -5))
        print(self.search([2,5],5))
        print(self.search([-1, 0, 5],5))
        print(self.search([-1, 0, 3, 5, 9, 12],9))
        print(self.search([-1, 0, 5], 5))
        print(self.search([-1, 0, 3, 5, 9, 12],2))
        print(self.search([5], 5))



obj = Solution()
obj.main()