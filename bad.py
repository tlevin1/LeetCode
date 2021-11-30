'''
278. First Bad Version

You are a product manager and currently leading a team to develop a new product.Unfortunately, the
latest version of your product fails the quality check.Since each version is developed based
on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions[1, 2, ..., n] and you want to find out the first bad one, which
causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.Implement
a function to find the first bad version.You should minimize the number of calls to the API.

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true Then 4 is the first bad version.

Example 2:

Input: n = 1, bad = 1
Output: 1

Constraints:

1 <= bad <= n <= 231 - 1
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Approach: use binary search to check versions
        #check mid is good if so check right if not check left

        #starting at 1
        l,r = 1,n

        if self.isBadVersion(l):
            return l

        while l < r:

            mid = (l + r)//2
            print('mid is', mid)

            if self.isBadVersion(mid):
                # second scenario where mid is true so recurse only on left
                r = mid


            else:
                # first scenario so recurse only on right
                l = mid + 1

        return l


    def isBadVersion(self,version):
        if version == 4:
            print('version',version)
            return True
        return False

    def main(self):
        print(self.firstBadVersion(5))
        print(self.firstBadVersion(1))
        print(self.firstBadVersion(2))
        print(self.firstBadVersion(4))

obj = Solution()
obj.main()