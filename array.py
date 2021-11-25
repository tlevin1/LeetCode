'''Given an array, return another array with just the ordered unique elements from the given array.
In other words, you're removing any duplicates.

Note: Order needs to be preserved, so no sorting should be done.
And the order should be maintained with the first occurrence of the element in the given array.'''
class Solution:
    def remove_dupes(self,arr):
        #approach: hash each element in array in another if not already found
        #return second array
        hash = []
        count = 0
        for i in range(len(arr)):
            if arr[i] not in hash:
                hash.append(arr[i])
        return hash

    def main(self):
        print(self.remove_dupes([1,2,3,1,5,4,3]))
        print(self.remove_dupes([9, 0, 11, 16, 19, 14, 7, 18, 10, 6, 0, 17, 12, 9, 12, 18, 0, 14, 17]))

obj = Solution()
obj.main()
