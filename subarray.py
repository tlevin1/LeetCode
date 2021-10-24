import sys
class Solution(object):
    def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # divide and conquer
        # using Kadanes algorithm

        # variable to keep track of max sum so far
        #using maxsize instead of maxint since python3
        max_so_far = -sys.maxsize - 1
        # print(max_so_far)
        # variable to keep track of segment
        max_ending_here = 0

        for i in range(len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if max_so_far < max_ending_here:
                # update max so far
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

    if __name__ == '__main__':
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        print(maxSubArray(nums))


