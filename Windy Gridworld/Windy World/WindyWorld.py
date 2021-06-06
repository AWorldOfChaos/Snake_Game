import random
import time
from matplotlib import pyplot as plt


class Env:
    def __init__(self):
        self.wind = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

    def action_result(self, initial_location, action_taken):
        row, col = initial_location
        row = row - self.wind[col]
        if action_taken == 0:
            row -= 1
        elif action_taken == 1:
            col -= 1
        elif action_taken == 2:
            row += 1
        elif action_taken == 3:
            col += 1
        if row < 0:
            row = 0
        elif row > 6:
            row = 6
        if col < 0:
            col = 0
        elif col > 9:
            col = 9
        final_location = [row, col]
        return final_location


class State:
    def __init__(self, row, col):
        self.values = [0]*4
        self.coordinates = [row, col]


class Agent:
    def __init__(self):
        self.model = Env()
        self.row = 3
        self.col = 0
        self.episode_complete = False
        self.states = []
        the_row = []
        for i in range(7):
            for j in range(10):
                the_row.append(State(i, j))
            self.states.append(the_row)
            the_row = []
        self.current_state = self.states[self.row][self.col]
        self.next_state = self.states[self.row][self.col]

    def sarsa_episode(self, step_size, gamma, display_actions):
        action_taken = 0
        while not self.episode_complete:
            if self.col == 7 and self.row == 3:
                self.episode_complete = True
                self.row = 3
                self.col = 0
                self.current_state = self.states[self.row][self.col]
                self.next_state = self.states[self.row][self.col]
            else:
                epsilon = 0.1
                if random.random() <= epsilon:
                    action_taken = random.randint(0, 3)
                else:
                    action_taken = self.current_state.values.index(max(self.current_state.values))

                final_loc = self.model.action_result([self.row, self.col], action_taken)
                self.row = final_loc[0]
                self.col = final_loc[1]
                self.next_state = self.states[self.row][self.col]

                q1 = epsilon * sum(self.current_state.values)/4 + (1 - epsilon) * max(self.current_state.values)
                q2 = gamma * (epsilon * sum(self.next_state.values)/4 + (1 - epsilon) * max(self.next_state.values))
                self.current_state.values[action_taken] += step_size * (-1 + q2 - q1)

                if display_actions:
                    # print(self.current_state.coordinates,self.next_state.coordinates)
                    x_change = int(self.next_state.coordinates[1] - self.current_state.coordinates[1])
                    if x_change < 0:
                        file.write("W ")
                    elif x_change > 0:
                        file.write("E ")
                    y_change = int(self.next_state.coordinates[0] - self.current_state.coordinates[0])
                    if y_change < 0:
                        for change in range(-y_change):
                            file.write("N ")
                    elif y_change > 0:
                        for change in range(y_change):
                            file.write("S ")

                self.current_state = self.states[self.row][self.col]

        self.episode_complete = False


file = open(r"Windy Solution.txt", "w")
step_size = 0.5
times = [0]*150
for j in range(100):
    agent = Agent()
    start_time = time.time()
    for i in range(150):
        times[i] += 25000*(time.time() - start_time)
        agent.sarsa_episode(0.5, 1, False)

agent = Agent()
agent.sarsa_episode(0.5, 1, False)
episodes = list(range(0, 150, 1))
plt.xlabel("Time Steps")
plt.ylabel("Episodes")
plt.plot(times, episodes)
plt.savefig('Windy World.png', dpi=300, bbox_inches='tight')
