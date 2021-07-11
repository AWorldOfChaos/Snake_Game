import numpy as np


class State:
    def __init__(self, state_val):
        self.state_num = state_val
        self.state_value = 0
        self.best_action = 0

    def state_value_eval(self, data, state_values, end_state, discount):
        if self.state_num in end_state:
            self.state_value = 0
            return
        counter = 0
        value = [0]*4
        action_possible = [False]*4
        for i in range(self.state_num, len(data)):
            if int(data[i][1]) == self.state_num:
                counter += 1
                value[int(data[i][2])] += (discount*state_values[int(data[i][3])] + float(data[i][4]))\
                                          * float(data[i][5])
                action_possible[int(data[i][2])] = True
            elif counter > 0:
                break
        max_value = -10000
        for i in range(len(value)):
            if max_value < value[i] and action_possible[i]:
                max_value = value[i]
        self.best_action = value.index(max_value)
        self.state_value = max_value


input_loc = input("Enter location of Encoded Maze")
# file = open(r"D:\pythonProject\venv\Maze Solver\data\EncodedMaze.txt", "r")
file = open(input_loc, "r")
mdp = []
end_states = []
data = []
state_values_new = []

st = file.readline()
lst = st.split()
num_states = int(lst[1])
for i in range(num_states):
    mdp.append(State(i))
    state_values_new.append(0)

st = file.readline()
lst = st.split()
num_actions = int(lst[1])

st = file.readline()
lst = st.split()
start_state = int(lst[1])

st = file.readline()
lst = st.split()
for x in lst:
    if x != "end":
        end_states.append(int(x))

while True:
    st = file.readline()
    lst = st.split()
    if lst[0] != "transition":
        break
    else:
        data.append(lst)

discount_line = file.readline()
lst = discount_line.split()
gamma = float(lst[1])
state_values_old = state_values_new.copy()
rtoll = 0
atol = 1e-11
while True:
    for obj in mdp:
        obj.state_value_eval(data, state_values_old, end_states, gamma)
        state_values_new[obj.state_num] = mdp[obj.state_num].state_value
    if np.allclose(np.array(state_values_new), np.array(state_values_old), rtoll, atol):
        break
    else:
        state_values_old = state_values_new.copy()
for i in range(num_states):
    print(state_values_new[i], mdp[i].best_action)
output_loc = input("Enter output location of encoded policy")
# file2 = open(r"D:\pythonProject\venv\Maze Solver\data\OptimalPolicy.txt", "w")
file2 = open(output_loc, "w")
for i in range(num_states):
    file2.write(str(state_values_new[i]))
    file2.write(" ")
    file2.write(str(mdp[i].best_action))
    file2.write("\n")
