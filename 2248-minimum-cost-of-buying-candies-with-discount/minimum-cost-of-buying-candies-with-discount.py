import heapq

class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        cost.sort(reverse=True)
        total_cost = 0

        counter = 0

        for i in range(0, len(cost)):
            if counter < 2:
                total_cost += cost[i]
                counter += 1
            else:
                counter = 0
        
        return total_cost