""""
A company is planning to interview 2n people.Given the array costs where
costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the
cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Example 1:

Input: costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
Output: 110
Explanation: The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
interviewing in each city.
Example 2:

Input: costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
Output: 1859

Example 3:

Input: costs = [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]
Output: 3086

Constraints:

2 * n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCosti, bCosti <= 1000

"""""
from typing import List

class Solution:

    #greedy approach
    #sort by price A - price B send first n (smallest price A - B) to A and rest to B
    #price A - price B = companys additional costs

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

       print(costs)
       # calculate cost for each person
       min_c = [(a-b) for a,b in costs]

       #sort based on gain A- B, getting ordered difference of A - B
       sorted_min = sorted((value,i) for (i,value) in enumerate (min_c))
       print(sorted_min)

       total_cost = 0
       n = len(costs)//2

        #send to A since costs alot for B for n smallest cost A - B
       for value, i in sorted_min[:n]:
          total_cost += costs[i][0]
        #send to B since costs alot for A for n smallest cost A - B
       for value,i in sorted_min[n:]:
          total_cost += costs[i][1]
       return total_cost


       #sort is n log n
       # constant space

    def main(self):
        costs = [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]
        min = self.twoCitySchedCost(costs)
        print(min)

obj = Solution()
obj.main()
