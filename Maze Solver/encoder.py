class Action:
    def __init__(self, num, state_one, state_two):
        self.action_num = num
        self.probability = 1.0
        self.start_state = state_one
        self.end_state = state_two
        self.reward = -1.0


class State:
    def __init__(self, state_num, row_num, column_num):
        self.num = state_num
        self.row = row_num
        self.column = column_num

    def decide_actions(self, state_matrix, action, end_state_value):
        if self.num == end_state_value:
            return
        for i in range(len(state_matrix)):
            if state_matrix[i].column == self.column + 1 and state_matrix[i].row == self.row:
                action.append(Action(3, state_matrix[self.num], state_matrix[i]))
            elif state_matrix[i].column == self.column - 1 and state_matrix[i].row == self.row:
                action.append(Action(1, state_matrix[self.num], state_matrix[i]))
            elif state_matrix[i].row == self.row + 1 and state_matrix[i].column == self.column:
                action.append(Action(2, state_matrix[self.num], state_matrix[i]))
            elif state_matrix[i].row == self.row - 1 and state_matrix[i].column == self.column:
                action.append(Action(0, state_matrix[self.num], state_matrix[i]))


input_loc = input()
file = open(input_loc, "r")
maze = []
while True:
    st = file.readline()
    if st == "":
        break
    else:
        lst = st.split()
        maze.append(lst)

file.close()
location = input("Enter output location")
# file2 = open(r"D:\pythonProject\venv\Maze Solver\data\EncodedMaze.txt", "w")
file2 = open(location, "w")
maze_height = len(maze)
maze_width = len(maze[0])
states = []
actions = []
num_actions = 4
start_state_num = 0
end_state_num = 0

for i in range(maze_height):
    for j in range(maze_width):
        if maze[i][j] == "0":
            states.append(State(len(states), i, j))
        if maze[i][j] == "2":
            states.append(State(len(states), i, j))
            start_state_num = len(states) - 1
        if maze[i][j] == "3":
            states.append(State(len(states), i, j))
            end_state_num = len(states) - 1

num_states = len(states)
for i in range(len(states)):
    states[i].decide_actions(states, actions, end_state_num)

file2.write("numStates " + str(num_states) + "\n")
file2.write("numActions " + str(num_actions) + "\n")
file2.write("start " + str(start_state_num) + "\n")
file2.write("end " + str(end_state_num) + "\n")

for i in range(len(actions)):
    file2.write("transition"
                + " " + str(actions[i].start_state.num)
                + " " + str(actions[i].action_num)
                + " " + str(actions[i].end_state.num)
                + " " + str(actions[i].reward)
                + " " + str(actions[i].probability) + "\n")
file2.write("mdptype episodic \n")
file2.write("discount 1.0")
