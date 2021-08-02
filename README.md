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

Snake Game
├── Maze Solver
│   ├── MazeVerifyOutput.py
│   ├── PlannerVerifyOutput.py
│   ├── README.md
│   ├── data
│   │   ├── EncodedMaze.txt
│   │   ├── MazeSolution.txt
│   │   ├── OptimalPolicy.txt
│   │   ├── maze
│   │   │   ├── grid10.txt
│   │   │   ├── grid100.txt
│   │   │   ├── grid20.txt
│   │   │   ├── grid30.txt
│   │   │   ├── grid40.txt
│   │   │   ├── grid50.txt
│   │   │   ├── grid60.txt
│   │   │   ├── grid70.txt
│   │   │   ├── grid80.txt
│   │   │   ├── grid90.txt
│   │   │   ├── solution10.txt
│   │   │   ├── solution100.txt
│   │   │   ├── solution20.txt
│   │   │   ├── solution30.txt
│   │   │   ├── solution40.txt
│   │   │   ├── solution50.txt
│   │   │   ├── solution60.txt
│   │   │   ├── solution70.txt
│   │   │   ├── solution80.txt
│   │   │   └── solution90.txt
│   │   └── mdp
│   │       ├── All Locations.txt
│   │       ├── continuing-mdp-10-5.txt
│   │       ├── continuing-mdp-2-2.txt
│   │       ├── continuing-mdp-50-20.txt
│   │       ├── episodic-mdp-10-5.txt
│   │       ├── episodic-mdp-2-2.txt
│   │       ├── episodic-mdp-50-20.txt
│   │       ├── sol-continuing-mdp-10-5.txt
│   │       ├── sol-continuing-mdp-2-2.txt
│   │       ├── sol-continuing-mdp-50-20.txt
│   │       ├── sol-episodic-mdp-10-5.txt
│   │       ├── sol-episodic-mdp-2-2.txt
│   │       └── sol-episodic-mdp-50-20.txt
│   ├── decoder.py
│   ├── encoder.py
│   ├── generateMDP.py
│   ├── planner.py
│   └── visualize.py
├── README.md
├── Scripts
│   ├── Activate.ps1
│   ├── activate
│   ├── activate.bat
│   ├── deactivate.bat
│   ├── f2py.exe
│   ├── futurize-script.py
│   ├── futurize.exe
│   ├── pasteurize-script.py
│   ├── pasteurize.exe
│   ├── pip.exe
│   ├── pip3.9.exe
│   ├── pip3.exe
│   ├── pyi-archive_viewer.exe
│   ├── pyi-bindepend.exe
│   ├── pyi-grab_version.exe
│   ├── pyi-makespec.exe
│   ├── pyi-set_version.exe
│   ├── pyinstaller.exe
│   ├── python.exe
│   └── pythonw.exe
├── Snake AI
│   ├── .gitignore
│   ├── Advanced Agent.py
│   ├── Agent.py
│   ├── Environment.py
│   ├── Font
│   │   └── PoetsenOne-Regular.ttf
│   ├── Graphics
│   │   ├── apple.png
│   │   ├── body_bl.png
│   │   ├── body_br.png
│   │   ├── body_horizontal.png
│   │   ├── body_tl.png
│   │   ├── body_tr.png
│   │   ├── body_vertical.png
│   │   ├── head_down.png
│   │   ├── head_left.png
│   │   ├── head_right.png
│   │   ├── head_up.png
│   │   ├── tail_down.png
│   │   ├── tail_left.png
│   │   ├── tail_right.png
│   │   └── tail_up.png
│   ├── README.md
│   ├── Snake Game.py
│   ├── Sound
│   │   └── crunch.wav
│   ├── Untrained Agent.py
│   ├── __pycache__
│   │   └── Environment.cpython-39.pyc
│   ├── fruits_episodes.png
│   ├── fruits_episodes_hist.png
│   ├── qmatrix.npy
│   └── qmatrix2.npy
├── Snake Game
│   ├── Font
│   │   └── PoetsenOne-Regular.ttf
│   ├── Game.py
│   ├── Graphics
│   │   ├── apple.png
│   │   ├── body_bl.png
│   │   ├── body_br.png
│   │   ├── body_horizontal.png
│   │   ├── body_tl.png
│   │   ├── body_tr.png
│   │   ├── body_vertical.png
│   │   ├── head_down.png
│   │   ├── head_left.png
│   │   ├── head_right.png
│   │   ├── head_up.png
│   │   ├── tail_down.png
│   │   ├── tail_left.png
│   │   ├── tail_right.png
│   │   └── tail_up.png
│   ├── README.md
│   └── Sound
│       └── crunch.wav
├── Windy Gridworld
│   ├── King's Windy World
│   │   ├── King's Windy Solution.txt
│   │   ├── King's Windy World.png
│   │   ├── KingWindyWorld.py
│   │   └── The_grid.txt
│   ├── Windy Path.png
│   ├── Windy World
│   │   ├── The_grid.txt
│   │   ├── Windy Solution.txt
│   │   ├── Windy World.png
│   │   ├── WindySolution.txt
│   │   └── WindyWorld.py
│   └── WindyVisualize.py
├── pyvenv.cfg
└── requirements.txt

![Game Poster](https://handsontek.net/images/Teams/Snake/hero.png)