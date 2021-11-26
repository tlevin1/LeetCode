'''In securities research, an analyst will look at a number of attributes for a stock. One analyst
would like to keep a record of the highest positive spread between a closing price and the closing
price on any prior day in history. Determine the maximum positive spread for a stock given its price
history. If the stock remains flat or declines for the full period, return -1

Example 1:
px = [7,1,2,5]

Calculate the positive difference between each price and its predecessors:
-At the first quote, there is no earlier quote to compare to
-At the second quote, there was no earlier price that was lower
-At the third quote, the price is higher than the second quote
    2 - 1 = 1
- For the 4th quote, the price is higher than the 3rd and the 2nd quotes
    5 - 2 = 3
    5 - 1 = 4
- The maximum difference is 4

Example 2:
px = [7,5,3,1]
The price declines each quote, so there is never a difference greater than 0. In this case we return -1

'''

class Solution:
    #px = array of stock prices
    def maxDifference(self,px):
        #keep track of differences between every number and its pred

        max_diff = px[1] - px[0]
        #not needed - just used to check iterations
        hash = []

        for i in range(len(px)):
            for j in range(1, len(px)):
                hash.append(px[j] - px[i])
                if px[j] - px[i] > max_diff:
                    if j > i:
                        max_diff = px[j] - px[i]
        #print(hash)
        # #check if stays flat
        # if min(hash) == max(hash):
        #     print('equal')
        #     return -1

        #check if stock decreases throughout
        desc = True
        for i in range(0,len(px)-1):
            if px[i+1] > px[i]:
                desc = False
        if desc:
            return -1
        #returns max diff between 2 prices
        return max_diff

    def main(self):
        print(self.maxDifference([7,1,2,5]))
        print(self.maxDifference([7, 1, 1, 1]))
        print(self.maxDifference([7, 5, 3, 1]))
        print(self.maxDifference([2,3,10,2,4,8,1]))
        print(self.maxDifference([1, 1, 1, 1]))
obj = Solution()
obj.main()
