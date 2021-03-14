class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False]*cols for i in range(rows)]
        path_length = 0
        for i in range(rows):
            for j in range(cols):
                if self.has_path(board, i, j, word, path_length, visited):
                    return True
        return False

    def has_path(self, board, row, col, word, path_length, visited):
        
        if path_length == len(word):
            return True

        flag = False
        if row >= 0 and row < len(board) and col >= 0 and col < len(board[0])\
             and board[row][col] == word[path_length] and not visited[row][col]:
            path_length += 1
            visited[row][col] = True
            flag = self.has_path(board, row+1, col, word, path_length, visited) or\
                   self.has_path(board, row-1, col, word, path_length, visited) or\
                   self.has_path(board, row, col+1, word, path_length, visited) or\
                   self.has_path(board, row, col-1, word, path_length, visited)

            if not flag:
                path_length -= 1
                visited[row][col] = False
        
        return flag