class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m*n != r*c:
            return mat
        
        result = [[0]*c for _ in range(r)]

        idx = 0
        for i in range(0, m):
            for j in range(0, n): 
                p = idx // c
                q = idx % c
                result[p][q] = mat[i][j]
                idx += 1

        return result