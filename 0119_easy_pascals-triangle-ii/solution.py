from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]

        up_row = self.getRow(rowIndex -1);

        res = []
        for i in range(1, len(up_row)):
            res.append(up_row[i-1] + up_row[i])
        
        return [1] + res + [1]