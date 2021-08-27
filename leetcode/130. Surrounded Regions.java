// DFS
class Solution {
    public void solve(char[][] board) {
        int m = board.length, n = board[0].length;
        int[][] bool = new int[m][n];

        for (int i = 0; i < m; i++) {
            check(board, i, 0, bool);
            check(board, i, n - 1, bool);
        }

        for (int j = 0; j < n; j++) {
            check(board, 0, j, bool);
            check(board, m - 1, j, bool);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (bool[i][j] != 1) {
                    board[i][j] = 'X';
                }
            }
        }
    }

    void check(char[][] board, int a, int b, int[][] bool) {
        int m = board.length, n = board[0].length;
        if (a < 0 || a >= m || b < 0 || b >=n || bool[a][b] == 1) {
            return;
        }
        if (board[a][b] == 'O') {
            bool[a][b] = 1;
            check(board, a - 1, b, bool);
            check(board, a + 1, b, bool);
            check(board, a, b - 1, bool);
            check(board, a, b + 1, bool);
        }
    }
}
