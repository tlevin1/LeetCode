"""
You are given a string s and an integer k, a k duplicate removal consists of choosing
k adjacent and equal letters from s and removing them, causing the left and the right side
of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.It is guaranteed
that the answer is unique.

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There
's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa" Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.
"""


class Solution:
    #recursive solution to loop through string and find k duplicate characters
    def removeDuplicates(self, s: str, k: int) -> str:
       count_char = 1
       for i in range(1, len(s)):
           #increment char count
           if s[i] == s[i-1]:
               count_char+=1
           else:
               #reset
               count_char = 1
           #once found k chars
           if count_char == k:
               #remove from string
               s=s.replace(s[i-k+1:i+1],"")
               #recursive call until break out of loop
               return self.removeDuplicates(s,k)
        #once no more duplicates
       return s









# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"

    def main(self):
        s = "deeedbbcccbdaa"
        k = 3
        print(self.removeDuplicates(s,k))

obj = Solution()
obj.main()