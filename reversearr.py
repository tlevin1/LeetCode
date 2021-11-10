#Reverse subarray (from i to j) of array

def reverse(arr, i, j):
    #assuming i is starting index and reversing upto and including j
    #edge cases: [], i > j, negative i or j
    if not arr:
        return "empty list!"
    if i > j:
        return "invalid reverse!"
    if i < 0 or j < 0:
        return "invalid indices provided!"

    while i <= len(arr) and j >= 0:
        #once at last swap
        if i == j - 1:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            break
        #swap e/ element
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        # print(arr[i])
        # print(arr[j])
        i = i + 1
        j = j - 1
    #return arr reversed
    return arr

# time complexity: O(j) - number of elements iterating over

print(reverse([1, 2, 3, 4], 0, 3))
print(reverse([1, 2, 3, 4], 0, 1))
print(reverse([1, 2, 3, 4], 0, 0))
print(reverse([1, 2, 3, 4], 5, 6))
print(reverse([1, 2, 3, 4], 7, 1))
print(reverse([1, 2, 3, 4], -1, 1))
print(reverse([], 0, 1))


