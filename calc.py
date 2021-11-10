'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open
'(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the
range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
 such as eval().



Example 1:

Input: s = "1+1"
Output: 2
Example 2:

Input: s = "6-4/2"
Output: 4
Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
Example 4:

Input: s = "(2+6*3+5-(3*14/7+2)*5)+3"
Output: -12
Example 5:

Input: s = "0"
Output: 0


Constraints:

1 <= s <= 104
s consists of digits, '+', '-', '*', '/', '(', and ')'.
s is a valid expression.


'''

from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        #using queue to compute mathematical expressions
        q = deque(s.replace(' ', ''))
        print(q)
        return self.calc_helper(q)

    def calc_helper(self, q):
        #stack to append calculated values to
        stack = []
        num=''
        sign='+'
        #print(q)
        while q:
            x = q.popleft()
            #print(x)
            #beginning of expression
            if x == '(':
                num = self.calc_helper(q)
                #print(num)
            #just numbers
            if x.isnumeric():
                #print(x)
                num += x
                #print(num)
                #print(num)

            #just signs
            if not x.isnumeric() or not q:
                #print('here')
                if sign == '+':
                    stack.append(int(num))
                elif sign == '-':
                    stack.append(-1*int(num))
                elif sign == "*":
                    stack.append(stack.pop() * int(num))
                elif sign == '/':
                    stack.append(int(stack.pop() / int(num)))
                sign = x
                num = ''
                if x == ')':
                    break
            #print(stack)
        return sum(stack)

    def main(self):
        s = "1+1"
        #s = "6-4/2"
        print(self.calculate(s))


obj = Solution()
obj.main()