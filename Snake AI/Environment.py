import pygame
# import sys
import random
from pygame.math import Vector2
import os


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        filename = os.path.join(dirname, 'Graphics/head_up.png')
        self.head_up = pygame.image.load(filename).convert_alpha()
        filename = os.path.join(dirname, 'Graphics/head_down.png')
        self.head_down = pygame.image.load(filename).convert_alpha()
        filename = os.path.join(dirname, 'Graphics/head_right.png')
        self.head_right = pygame.image.load(filename).convert_alpha()
        filename = os.path.join(dirname, 'Graphics/head_left.png')
        self.head_left = pygame.image.load(filename).convert_alpha()

        filename = os.path.join(dirname, 'Graphics/tail_up.png')
        self.tail_up = pygame.image.load(filename).convert_alpha()
        filename = os.path.join(dirname, 'Graphics/tail_down.png')
        self.tail_down = pygame.image.load(filename).convert_alpha()
        filename = os.path.join(dirname, 'Graphics/tail_right.png')
        self.tail_right = pygame.image.load(filename).convert_alpha()
        filename = os.path.join(dirname, 'Graphics/tail_left.png')
        self.tail_left = pygame.image.load(filename).convert_alpha()

        filename = os.path.join(dirname, 'Graphics/body_vertical.png')
        self.body_vertical = pygame.image.load(filename).convert_alpha()
        filename = os.path.join(dirname, 'Graphics/body_horizontal.png')
        self.body_horizontal = pygame.image.load(filename).convert_alpha()

        filename = os.path.join(dirname, 'Graphics/body_tr.png')
        self.body_tr = pygame.image.load(filename).convert_alpha()
        filename = os.path.join(dirname, 'Graphics/body_tl.png')
        self.body_tl = pygame.image.load(filename).convert_alpha()
        filename = os.path.join(dirname, 'Graphics/body_br.png')
        self.body_br = pygame.image.load(filename).convert_alpha()
        filename = os.path.join(dirname, 'Graphics/body_bl.png')
        self.body_bl = pygame.image.load(filename).convert_alpha()
        filename = os.path.join(dirname, 'Sound/crunch.wav')
        self.crunch_sound = pygame.mixer.Sound(filename)

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
            return True

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
            return True

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                return True

    def game_over(self):
        self.snake.reset()

    @staticmethod
    def draw_grass():
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,
                              apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)

os.getcwd()
dirname = os.path.dirname(__file__)
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
filename = os.path.join(dirname, 'Graphics/apple.png')
apple = pygame.image.load(filename).convert_alpha()
game_font = pygame.font.SysFont('comicsansms', 25)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# main_game = Game()
#    screen.fill((175, 215, 70))
#    main_game.draw_elements()
#    pygame.display.update()
#    clock.tick(60)
