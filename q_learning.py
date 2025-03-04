import random
from tic_tac_toe import TicTacToe

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {} 
        self.alpha = alpha 
        self.gamma = gamma 
        self.epsilon = epsilon 

    def get_state(self, board):
        return tuple(tuple(row) for row in board)

    def available_actions(self, board):
        return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

    def choose_action(self, board):
        state = self.get_state(board)
        valid_actions = self.available_actions(board)
        
        if random.random() < self.epsilon or state not in self.q_table:
            return random.choice(valid_actions)
        
        q_values = {a: self.q_table[state][a] for a in valid_actions if a in self.q_table[state]}
        return max(q_values, key=q_values.get) if q_values else random.choice(valid_actions)

    def update_q(self, state, action, reward, next_state):
        state, next_state = self.get_state(state), self.get_state(next_state)
        state_list = [list(row) for row in state] 
        next_state_list = [list(row) for row in next_state] 


        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in self.available_actions(state_list)}
        if next_state not in self.q_table:
            self.q_table[next_state] = {a: 0 for a in self.available_actions(next_state_list)}
        if action not in self.q_table[state]:
            self.q_table[state][action] = 0
        
        best_next_q = max(self.q_table[next_state].values(), default=0) 
        self.q_table[state][action] += self.alpha * (reward + self.gamma * best_next_q - self.q_table[state][action])
