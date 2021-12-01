"""
977. Squares of a Sorted Array
Given an integer array nums sorted in non - decreasing order, return an array
of the squares of each number sorted in non - decreasing order.

Example 1:

Input: nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
Explanation: After squaring, the array becomes[16, 1, 0, 9, 100].
After sorting, it becomes[0, 1, 9, 16, 100].

Example 2:

Input: nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non - decreasing
order.

Follow up: Squaring each element and sorting the new array is very
trivial, could you find an O(n) solution using a different approach?
"""
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    #Approach: brute force - square every number then sort entire array
    #runtime: O(n) + O(n log n)

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        ans = sorted(nums)
        return ans

    #Another way
    #return sorted(x * x for x in A)

    #O(N) approach: since input array is already sorted can see that we can ignore negative signs since
    # the neg numbers become large. So we know largest value in arr is in first element or last. Two pointer
    #approach
    #compare abs(l) and abs(r) if left < right then square will be bigger so square and add to new array
    #move pointer for element only if inserted to new array

    def sortedSquares2(self, nums: List[int]) -> List[int]:

        left = 0
        right = len(nums) - 1

        #initialized to zeros so can easily store squares
        ans = [0] * len(nums)

        #Only way found for iterating array starting at end
        for i, e in reversed(list(enumerate(nums))):
            if abs(nums[left]) < abs(nums[right]):
                sq = nums[right]
                right = right - 1
            else:
                sq = nums[left]
                left = left + 1

            ans[i] = (sq * sq)
        return ans

    def main(self):
        print(self.sortedSquares([-7, -3, 2, 3, 11]))
        print(self.sortedSquares2([-7, -3, 2, 3, 11]))

obj = Solution()
obj.main()