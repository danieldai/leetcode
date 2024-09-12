from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]

        direction = 1

        i = j = 0

        for v in range(1, n*n + 1):
            result[i][j] = v
            if direction == 1:
                if j+1 < n and result[i][j+1] == 0:
                    j += 1
                else:
                    i += 1
                    direction = 2
            elif direction == 2:
                if i+1 < n and result[i+1][j] == 0:
                    i += 1
                else:
                    j -= 1
                    direction = 3
            elif direction == 3:
                if j-1 >= 0 and result[i][j-1] == 0:
                    j -= 1
                else:
                    i -= 1
                    direction = 4
            else:
                if i-1 >= 0 and result[i-1][j] == 0:
                    i -= 1
                else:
                    j += 1
                    direction = 1

        return result
        