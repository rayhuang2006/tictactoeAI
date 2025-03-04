class TicTacToe:
    def __init__(self):
        self.board = [[0] * 3 for _ in range(3)]
        self.current_player = 1 

    def reset(self):
        self.board = [[0] * 3 for _ in range(3)]
        self.current_player = 1
        return self.board

    def step(self, action):
        x, y = action
        if self.board[x][y] != 0:
            return self.board, -10, False

        self.board[x][y] = self.current_player
        reward = self.check_winner()
        done = reward != 0 or all(cell != 0 for row in self.board for cell in row)

        self.current_player *= -1 
        return self.board, reward, done

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]

        return 0
    def render(self):
        for row in self.board:
            print(row)

# 測試
game = TicTacToe()
game.render()