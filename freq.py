# Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array.
# Return the array of these digits in ascending order.
# Example
# For a = [25, 2, 3, 57, 38, 41], the output should be mostFrequentDigits(a) = [2, 3, 5].

# The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5.
# So the answer is [2, 3, 5].

# Guaranteed constraints:
# 1 ≤ a.length ≤ 103,
# 1 ≤ a[i] < 100.
# [output] array.integer
# The array of most frequently occurring digits, sorted in ascending order.

def mostFrequentDigits(a):
    #histogram array - keeps track of counts of each digit
    arr = [0] * 10
    #loop over passed in array
    for i in range(len(a)):
        #using modulus - divide to get digits of each integer
        num = a[i]
        #get each digit and update count in array
        #looping while true and not while num > = 0 in order to account for #0 itself
        while True:
            #get last digit - msb
            digit = num % 10
            arr[digit] += 1
            # get other digits
            num = num // 10
            if num <= 0:
                break

    #solution array to store all the most frequent digits
    sol = []
    #get max from array - highest digits, can be multiple
    maxi = max(arr)
    #add highest freq digits to solution array
    for i in range(len(arr)):
       if arr[i] == maxi:
           sol.append(i)
    return sol


#test input
#a =  [25, 2, 3, 57, 38, 41]
a =  [0, 4, 4530, 57, 38, 70]
#a = [25,222,3,57,38,41]
print(mostFrequentDigits(a))

