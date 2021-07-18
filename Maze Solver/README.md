
This assignment covers the implementation of a maze solver using Value Iteration.

The assignment has two parts, in the first part we use the value iteration algorithm on an MDP. And in the second part we model our maze as an MDP and then attempt to solve it. In the data folder, you'll find the data for the maze as well as the mdp.

[Link to Assignment 1](https://www.cse.iitb.ac.in/~shivaram/teaching/old/cs747-a2020/pa-2/programming-assignment-2.html)

## The main files
- The planner.py file runs the Value Iteration algorithm and assigns a value to each element which can then be used for further analysis.
- The encoder.py file encodes the maze 
- The decoder.py file then understands the output of the planner file and decides the shortest path between given points of a given maze.