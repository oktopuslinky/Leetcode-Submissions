class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        output = [[1], [1,1]]
        if numRows < 3:
            return output[:numRows]

        for rowNum in range(2, numRows):
            prevRow = output[rowNum-1]
            newRow = [1]
            for i in range(1, len(prevRow)):
                newRow.append(prevRow[i] + prevRow[i-1])
            newRow.append(1)
            output.append(newRow)

        return output