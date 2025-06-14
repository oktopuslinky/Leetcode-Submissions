class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        
        '''
        status: if box is open/closed
        candies: number of candies in box
        keys: boxes you can open after opening this one (update status for boxes to 1)
        containedBoxes: boxes found inside this box. (adjacent nodes)
        '''

        stack = initialBoxes[:] # boxes to explore, current candies
        backlog = [] # added to when box is closed
        totalCandies = 0
        while stack or backlog:
            startStack = stack[:] # to check if any change was made

            # stack loop
            while stack:
                curBox = stack.pop()
                
                if status[curBox] != 0:
                    foundBoxes = containedBoxes[curBox]
                    stack += foundBoxes
                    newUnlocked = keys[curBox]
                    for box in newUnlocked:
                        status[box] = 1

                    totalCandies += candies[curBox]
                else:
                    backlog.append(curBox)

            # backlog loop
            while backlog:
                curBox = backlog.pop()
                if status[curBox] != 0:
                    foundBoxes = containedBoxes[curBox]
                    backlog += foundBoxes
                    newUnlocked = keys[curBox]
                    for box in newUnlocked:
                        status[box] = 1

                    totalCandies += candies[curBox]
                else:
                    stack.append(curBox)


            if stack == startStack: # if no change was made, exit
                break

        return totalCandies