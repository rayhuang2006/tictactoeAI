import random
from tic_tac_toe import TicTacToe
from q_learning import QLearningAgent

def print_board(board):
    symbols = {1: "X", -1: "O", 0: " "}
    for row in board:
        print(" | ".join(symbols[cell] for cell in row))
        print("-" * 9)

def play():
    env = TicTacToe()
    agent = QLearningAgent()
    
    import pickle
    try:
        with open("q_table.pkl", "rb") as f:
            agent.q_table = pickle.load(f)
    except FileNotFoundError:
        print("Q 表未找到，請先訓練 AI！")
        return

    state = env.reset()
    done = False

    if random.choice([True, False]):
        env.current_player = 1 
        print("人類先手！")
    else:
        env.current_player = -1 
        print("AI 先手！")

    print("井字棋遊戲開始！")
    print_board(state)

    while not done:
        if env.current_player == 1:
            while True:
                try:
                    x, y = map(int, input("輸入你的行動 (行 列，例如 '0 1'): ").split())
                    if (x, y) in agent.available_actions(state):
                        break
                    print("非法移動，請重新輸入！")
                except ValueError:
                    print("輸入格式錯誤，請輸入兩個數字，例如 '0 1'")

            state, _, done = env.step((x, y))

        else:  # AI 行動
            action = agent.choose_action(state)
            print(f"AI 選擇: {action}")
            state, _, done = env.step(action)

        print_board(state)

    print("遊戲結束！")
    winner = env.check_winner()
    if winner == 1:
        print("你贏了！")
    elif winner == -1:
        print("AI 贏了！")
    else:
        print("平局！")

if __name__ == "__main__":
    play()