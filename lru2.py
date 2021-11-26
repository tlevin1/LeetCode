'''Design a data structure that follows the constraints of a Least Recently Used(LRU) cache.

Implement the LRUCache class:


LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value) Update the value of the key if the key exists.Otherwise, add
the key - value pair to the cache.If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1 = 1}
lRUCache.put(2, 2); // cache is {1 = 1, 2 = 2}
lRUCache.get(1); // return 1
lRUCache.put(3, 3); // LRU
key was 2, evicts key 2, cache is {1 = 1, 3 = 3}
lRUCache.get(2); // returns - 1(not found)
lRUCache.put(4, 4); // LRU
key was 1, evicts key 1, cache is {4 = 4, 3 = 3}

lRUCache.get(1); // return -1(not found)
lRUCache.get(3); // return 3
lRUCache.get(4); // return 4

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
'''

from collections import OrderedDict


class LRUCache:
    #Approach: place keys in cache or update existing key value, for every get or put we move the key to the end to
    #keep track of the LRU/MRU items (LRU at front of ordered dict and MRU at end). Once we reach our capacity, we remove
    #an element from the front as it is the LRU item.

    #initialize cache with positive capacity

    def __init__(self,capacity:int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put_key(self, key:int, value:int) -> None:
        self.cache[key] = value
        #LRU items at beginning and MRU at end
        self.cache.move_to_end(key)
        #full
        if self.capacity < len(self.cache):
            #print('here')
            #removes from front - LRU items
            self.cache.popitem(last = False)


    #returns value of key if exists else -1
    def get_key(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache.get(key)
        return -1

cache = LRUCache(2)
cache.put_key(1, 1)
print(cache.get_key(1))
print(cache.cache)
cache.put_key(2, 2)
print(cache.get_key(1))
print(cache.cache)
cache.put_key(3, 3)
print(cache.cache) # cache is {1 = 1, 3 = 3}
print(cache.get_key(2)) #returns - 1(not found)
cache.put_key(4, 4)
print(cache.cache) #key was 1, evicts key 1, cache is {3 = 3,4=4}
print(cache.get_key(1)) # return -1(not found)
print(cache.get_key(3)) # return 3
print(cache.get_key(4)) # return 4


