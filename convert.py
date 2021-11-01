# Given an integer num, return a string of its base 7 representation.
#
# Example 1:
#
# Input: num = 100
# Output: "202"
# Example 2:
#
# Input: num = -7
# Output: "-10"
#
# Constraints: -107 <= num <= 107

class Solution:
    def convertToBase7(self, num: int) -> str:

        #account for number 0
        if num == 0:
            return "0"

        res = []
        rem = 0
        neg = False
        done = False

        # adding to account for negative numbers
        if num < 0:
            num = num * -1
            neg = True
            print('I shouldnt be here')

        #append remainder and quotient
        while num:
                res.append(str(num % 7))
                num = num // 7
                print(num)


        #print(res)
        # convert list to string
        stri = [str(integer) for integer in res]
        print(stri)

        if neg:
            a_string = "".join(stri)
            #reverse before return
            a_string = a_string[::-1]
            a_string = '-' + a_string

        else:
            #reverse before return
            a_string = "".join(reversed(stri))


        # return as string
        return a_string


    def main(self):
        num = -7
        print(self.convertToBase7(num))

Object = Solution()
Object.main()




