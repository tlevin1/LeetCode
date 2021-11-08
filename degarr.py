"""
Given a non - empty array of non - negative integers nums, the degree of this
array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a(contiguous) subarray
of nums, that has the same degree as nums.

Example 1:

Input: nums = [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:

Input: nums = [1, 2, 2, 3, 1, 4, 2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So[2, 2, 3, 1, 4, 2] is the shortest subarray, therefore returning 6.

Constraints:

nums.length will be between 1 and 50, 000.
nums[i] will be an integer between 0 and 49, 999.
"""
from collections import defaultdict
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        #started by trying it with default dict of type int but found easier with type list
        # appearances = defaultdict(int)
        # for curr in nums:
        #     appearances[curr] += 1
        #
        # print(appearances)
        # all_values = appearances.values()
        # degree = max(all_values)
        # print(degree)

        #using a defualt dict of type list to get the ranges of occurences
        count_dict = defaultdict(list)
        #print(count_dict)


        for i,x in enumerate(nums):
            #print(nums[i])
            count_dict[x].append(i)
            print(count_dict[x])

        #list of ranges for each value
        print(count_dict)
        # print(count_dict.values())
        # print(count_dict.keys())

        #degree = max freq of any element
        #list comprehension to get highest degree which = the max sublength
        degree = max([len(q) for q in count_dict.values()])


        #print(degree)

        sol = len(nums)
        for val in count_dict.values():
            if len(val) == degree:
                #print(v[1])
                #print(v[0]-1)
                sol = min(sol, val[-1]-val[0]+1)
                #print(sol)

        #print(sol)
        return sol

        #get min range sublength using list comprehension - fancy shorter way
        #return min(i[-1] - i[0] for i in count_dict.values() if len(i) == degree) + 1



    def main(self):
        nums = [1, 2, 2, 3, 1]
        #nums = [1]
        #nums = [0]
        print(self.findShortestSubArray(nums))


obj = Solution()
obj.main()