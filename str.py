'''
We're given a string and need to see if it can be broken down into words
from a dictionary array. For example:

JAVASCRIPT:
const str = "applecomputer";
const dictArr = ["apple", "computer"];
stringBreakdown(str, dictArr);
// true

Assuming that there are no repeats in the dictionary array, can you write a method that will
 return true if the string can be broken down into words from the array, or false if not?


Constraints
Length of the string <= 1000
The string is made up of ASCII characters (all or some of it)
Expected time complexity : O(n^2)
Expected space complexity : O(n)
'''
class Solution:
    def stringBreakdown(self,str,dictArr):
        #Approach 1:
        # iterate over dict and string - recursively check each word using dfs
        #if the first letter in the word in the dict is in str(prefix check) then check rest
        #Approach 2:
        #using dynamic programming/dict
        n = len(str)
        #initialze table to false - table to mark if index is reachable or not
        dp = [False for _ in range(n + 1)]
        #can reach 0 index of every string
        dp[0] = True

        for i in range(n):
            if dp[i]:
                for word in dictArr:
                    if str[i:i + len(word)] == word:
                        print(str[i:i + len(word)])
                        dp[i + len(word)] = True
        print(dp[-1])
        return dp[-1]

    def main(self):
        str = "applecomputer"
        dictArr = ["apple", "computer"]
        print(self.stringBreakdown(str,dictArr))

obj = Solution()
obj.main()

'''
Explainantion:
* For this we can use dp to mark the index which is reachable or not.
* In starting we can reach the 0th index of any string so make it True.
* Now, start the loop of length of given string and when you find the index is reachable i.e. **dp[i]==True** start checking for the next word to be fitted in string.
* If found make dp[i]=True.
* By going all the index if we are unable to reach last index then it will remain as False.
* Return the dp[-1] which will signify that we are able form string or not from wordDictionary given.
'''