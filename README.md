# tictactoeAI

This is a tic-tac-toe game AI implemented using Q-learning algorithm. The project includes the basic logic of the tic-tac-toe game, the implementation of the Q-learning agent, as well as scripts and Jupyter Notebooks for training and testing AI.

## Project structure 

- `tic_tac_toe.py`: Contains the basic logic of the Tic-Tac-Toe game, including board initialization, step processing and victory checking.
- `q_learning.py`: Implements the Q-learning agent, including state representation, action selection and Q-value update.
- `test.py`: Script for testing AI, allowing human players to play against AI.
- `rl.ipynb`: Jupyter Notebook for training AI, including the training process and Q-table storage.
- `q_table.pkl`: trained Q table, used to load and test AI in `test.py`.

## Usage 

### 1. Train AI 

Open `rl.ipynb`  
Run all cells to rain AI   
Save the Q table.  

### 2. Test AI ​​

run `test.py` to play against the trained AI.
