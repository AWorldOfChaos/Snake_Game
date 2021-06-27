import Environment as E
import pygame
import random
from pygame.math import Vector2


class Agent:
    def __init__(self):
        self.env = E.Game()
        self.actions = [0, 1, 2, 3]
        self.state = self.state_locator()
        self.qmatrix = [[0 for i in range(4)] for j in range(16)]

    def state_locator(self):
        x1 = self.env.fruit.x > self.env.snake.body[0].x
        y1 = self.env.fruit.y > self.env.snake.body[0].y
        x2 = self.env.fruit.x < self.env.snake.body[0].x
        y2 = self.env.fruit.y < self.env.snake.body[0].y
        return 8*x1 + 4*y1 + 2*x2 + y2

    def greedy_action(self):
        action_val = self.qmatrix[self.state]
        return action_val.index(max(action_val))

    def state_value(self, epsilon):
        values = self.qmatrix[self.state]
        return (1-epsilon)*max(values)+epsilon*sum(values)

    def exploration(self, current, action):
        reward = 1
        if current == 9:
            if action == 0 or action == 3:
                return reward
        elif current == 3:
            if action == 0 or action == 1:
                return reward
        elif current == 6:
            if action == 1 or action == 2:
                return reward
        elif current == 12:
            if action == 2 or action == 3:
                return reward
        elif current == 1:
            if action == 0:
                return reward
        elif current == 2:
            if action == 1:
                return reward
        elif current == 4:
            if action == 2:
                return reward
        elif current == 8:
            if action == 3:
                return reward
        return -reward

    def take_action(self, num):
        epsilon = 0.01
        gamma = 0.5

        while True:
            action = 0
            if random.random() < epsilon:
                action = random.choice(self.actions)
                print("Random")
            else:
                action = self.greedy_action()
                print("Greedy")

            if action == 0 and not self.env.snake.direction == Vector2(0, 1):
                self.env.snake.direction = Vector2(0, -1)
                break
            elif action == 1 and not self.env.snake.direction == Vector2(1, 0):
                self.env.snake.direction = Vector2(-1, 0)
                break
            elif action == 2 and not self.env.snake.direction == Vector2(0, -1):
                self.env.snake.direction = Vector2(0, 1)
                break
            elif action == 3 and not self.env.snake.direction == Vector2(-1, 0):
                self.env.snake.direction = Vector2(1, 0)
                break

        current = self.state
        self.env.snake.move_snake()
        reward = -0.1
        if self.env.check_fail():
            reward += -1000
        if self.env.check_collision():
            reward += 10
        reward += int(self.exploration(current, action))
        self.state = self.state_locator()
        final = self.state
        self.qmatrix[current][action] += gamma*(reward + self.state_value(epsilon) - self.qmatrix[current][action])
        print(final, num, reward)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
game_font = pygame.font.SysFont('comicsansms', 25)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

agent = Agent()
num = 0
while num < 10000:
    num += 1
    agent.take_action(num)
    screen.fill((175, 215, 70))
    agent.env.draw_elements()
    pygame.display.update()
    clock.tick(10)
print(agent.qmatrix)
