Snake AI
----------

### Problem Statement
To create a self-learning agent which will learn to play the [Snake Game](https://en.wikipedia.org/wiki/Snake_(video_game_genre)).

This repository contains the files and the code for my WnCC Summer of Code - 2021 Project (Snake AI)

In this project, I built the very popular Nokia Snake Game from scratch and then implemented basic Reinforcement Learning (RL) techniques to help the snake master the game and get really high scores. The RL agent is capable of learning on its own by exploring its environment to determine the best action to take in a certain situation.

### Resources Used
[Resources](https://www.notion.so/SOC-Snake-AI-Project-471ff57983a24f749ca0ec08df8c9472)

To download all the modules/packages used, simply run
```
pip install -r requirements.txt
```

Also, while running the following .py files, if they're not in the parent directory, enter the full path of the .py files.

There are 4 parts to this repository
## 1. Snake Game
This section covers an implementation of the Snake Game. Pygame has been used for the same. The associated graphics, sounds and fonts have been included in the same folder.
A demo of the game can be found [here](https://drive.google.com/drive/folders/1CTkxnkQnRemGd09Aj9upi3X7SBlZLHA-?usp=sharing)
To run this game, simply run
```
python Game.py
```
## 2. Maze Solver
The Maze solver section covers the model-based RL algorithms. There is a maze, details of which(transition matrix of the MDP) are entirely known to the agent. The agent uses this data to find the _shortest_ path through the maze. Some sample mazes and their solutions are provided as .txt files.
To run this section, follow the following steps,
- Run encoder.py and input the location of the .txt file containing the maze(gridfile)
- Run planner.py
- Run decoder.py. The solution is saved in 'data/MazeSolution.txt'

To visualise the maze, use this command, 
``` 
python visualize.py gridfile
```
To visualise your solution, use this command,
```
python visualize.py gridfile pathfile
```
## 3. GridWorld
The gridworld problem is a problem in which the agent has to be learn about the environment(model is not known). Using model-free algorithms, the agent tries to find its way from start to finish through the gridworld.

## 4. Simple Snake RL Agent
This is the main project. 
- To see the agent train, run Untrained Agent.py and see the agent become better gradually.
- To see the final trained agent, run Agent.py 

Details about the agent are as provided.
### State Space
My representation uses 12 bits of information to describe the current state of the snake:
- 4 bits of information to define the relative position of the fruit with respect to the head of the snake.
- 8 bits of information for obstacles in up, down, left, right and the diagonal directions.

### Action Space
The snake has 4 possible actions:

- Go Up
- Go Left
- Go Down
- Go Right
Hence our Q matrix has dimensions 8x15x4.
8 comes from the relative position of the fruit with respect to the head of the snake. 15 comes from the 4 bit obstacle space. 4 comes from the 4 actions.

### Reward Scheme
I have used a fairly simple reward scheme that can be optimized to improve the performance of the agent:
- Reward of +1 if the snake moves closer to the fruit
- Reward of -2 if the snake moves away from the fruit
- Reward of +30 for eating the fruit
- Reward of -300 for crashing into the wall or itself

### Hyperparameters
The discount factor and ε parameter for an ε-greedy policy are 0.5 and 0.1. Without decaying these hyperparameters, the training behaviour of the agent is extremely erratic. With annealing, the performance is more consistent. The agent has achieved a maximum score of 79.

The training time increases exponentially if we increase the state space (improve its vision).

### Training
We can get an idea about the training of our model by plotting the average number of fruits eaten by our snake in every 10 episodes as it trains.
For the obstacle state, the training graph is as follows:
![](.\Snake AI\fruits_episodes.png "Histogram").

### Trained Agent
We can plot a histogram of the number of fruits our agent consumes over a span of 300 episodes. This gives us an estimate of our performance. I've also added mean and max data outputs on the histogram itself.
![](.\Snake AI\fruits_episodes_hist.png "Histogram").
![Game Poster](https://handsontek.net/images/Teams/Snake/hero.png)
