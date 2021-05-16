file = open(r"D:\pythonProject\venv\Maze Solver\data\EncodedMaze.txt", "r")
file2 = open(r"D:\pythonProject\venv\Maze Solver\data\OptimalPolicy.txt", "r")
file3 = open(r"D:\pythonProject\venv\Maze Solver\data\MazeSolution.txt", "w")

data = []

st = file.readline()
lst = st.split()
num_states = int(lst[1])

st = file.readline()
lst = st.split()
num_actions = int(lst[1])

st = file.readline()
lst = st.split()
start_state = int(lst[1])

st = file.readline()
lst = st.split()
end_state = int(lst[1])

while True:
    st = file.readline()
    lst = st.split()
    if lst[0] != "transition":
        break
    else:
        data.append(lst)
file.close()

current_state = start_state
policy = []
while True:
    st = file2.readline()
    if st == "":
        break
    else:
        lst = st.split()
        policy.append(lst)
file2.close()

while True:
    if current_state == end_state:
        break
    action_taken = int(policy[current_state][1])
    for i in range(len(data)):
        if int(data[i][1]) == current_state and int(data[i][2]) == action_taken:
            current_state = int(data[i][3])
            if action_taken == 0:
                file3.write("N ")
            elif action_taken == 1:
                file3.write("W ")
            elif action_taken == 2:
                file3.write("S ")
            elif action_taken == 3:
                file3.write("E ")
            break
file3.close()
