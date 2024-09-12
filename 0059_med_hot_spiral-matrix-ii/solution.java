class Solution {
    public int[][] generateMatrix(int n) {
        int[][] result = new int[n][n];

        int i = 0;
        int j = 0;
        int direction = 1;

        for (int v = 1; v <= n*n; v++) {
            result[i][j] = v;

            if(direction == 1) {
                if (j+1 < n && result[i][j+1] == 0) {
                    j++;
                } else {
                    i++;
                    direction = 2;
                } 
            } else if (direction == 2) {
                if (i+1 < n && result[i+1][j] == 0) {
                    i++;
                } else {
                    j--;
                    direction = 3;
                }
            } else if (direction == 3) {
                if (j-1 >= 0 && result[i][j-1] == 0) {
                    j--;
                } else {
                    i--;
                    direction = 4;
                }
            } else {
                if (i-1 >= 0 && result[i-1][j] == 0) {
                    i--;
                } else {
                    j++;
                    direction = 1;
                }
            }

        }

        return result;

    }
}