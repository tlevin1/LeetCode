'''Given two integer arrays nums1 and nums2, return an array of their intersection.Each
element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2]
Example 2:

Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [9, 4]
Explanation: [4, 9] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000 '''
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #simple solution
        lst = [value for value in nums1 if value in nums2]
        #returns as a set - accepted
        return set(lst)
        #or can return as list
        # lst2 = set(lst)
        # lst2 = list(lst2)
        # return lst2


    def main(self):
        #find intersection of 2 lists
        # first way that came to mind
        l1 = [1,3,6,9,11]
        l2 = [1,4,9,12]
        #concat the lists
        joinedl = l1 + l2
        #1 & 9 are common elements
        #sort
        # O(n log n)
        joinedl.sort()
        print(joinedl)
        list = []
        #iterate and find dupes
        # O(n)
        for i in range(len(joinedl) - 1):
            if joinedl[i] == joinedl[i+1]:
                list.append(joinedl[i])
        print(list)
        # ^ This way wouldn't work if had duplicates in 1 list (unless convert each list to set at beginning )^
        #2nd simpler way
        lst = [value for value in l1 if value in l2]
        print(lst)

        #3rd more efficent solution
        # O(n)
        temp = set(l2)
        lst2 = [value for value in l1 if value in temp]
        print(lst2)

        print(self.intersection(l1, l2))


obj = Solution()
obj.main()
