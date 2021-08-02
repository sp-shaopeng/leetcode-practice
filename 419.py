class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        m = len(board)
        n = len(board[0])
        for i in range(m) :
            for j in range(n) :
                if(board[i][j] == "X" and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j - 1] == '.')):
                    count += 1
        return count