import pygame
import os
import random
import math
import numpy
import pygame_widgets
from pygame_widgets.button import Button
from pygame import Vector2
pygame.init()

WIDTH = 600
HEIGHT = 500

BG_COLOR = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rock Paper Scissors')
ROCK_IMG = os.path.join('assets', 'Rock.png')
PAPER_IMG = os.path.join('assets', 'Paper.png')
SCISSORS_IMG = os.path.join('assets', 'Scissors.png')
C_ROCK_IMG = os.path.join('assets', 'Rock_controlled.png')
C_PAPER_IMG = os.path.join('assets', 'Paper_controlled.png')
C_SCISSORS_IMG = os.path.join('assets', 'Scissors_controlled.png')

IMG_WIDTH = 40
IMG_HEIGHT = 40
standard_speed = 0.3
# selected_item = None
# control = 0

button = Button(
# Mandatory Parameters
    screen,  # Surface to place button on
    WIDTH - 110,  # X-coordinate of top left corner
    20,  # Y-coordinate of top left corner
    100,  # Width
    30,  # Height

    # Optional Parameters
    text='Add rock',  # Text to display
    fontSize=20,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(204, 229, 255),  # Colour of button when not being interacted with
    hoverColour=(204, 204, 255),  # Colour of button when being hovered over
    pressedColour=(102, 178, 255),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: myFunction1(final_list)  # Function to call when clicked on
)
button1 = Button(
# Mandatory Parameters
    screen,  # Surface to place button on
    WIDTH - 110,  # X-coordinate of top left corner
    60,  # Y-coordinate of top left corner
    100,  # Width
    30,  # Height

    # Optional Parameters
    text='Add paper',  # Text to display
    fontSize=20,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(204, 229, 255),  # Colour of button when not being interacted with
    hoverColour=(204, 204, 255),  # Colour of button when being hovered over
    pressedColour=(102, 178, 255),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: myFunction2(final_list)  # Function to call when clicked on
)
button2 = Button(
# Mandatory Parameters
    screen,  # Surface to place button on
    WIDTH - 110,  # X-coordinate of top left corner
    100,  # Y-coordinate of top left corner
    100,  # Width
    30,  # Height

    # Optional Parameters
    text='Add scissors',  # Text to display
    fontSize=20,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(204, 229, 255),  # Colour of button when not being interacted with
    hoverColour=(204, 204, 255),  # Colour of button when being hovered over
    pressedColour=(102, 178, 255),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: myFunction3(final_list)  # Function to call when clicked on
)
button3 = Button(
# Mandatory Parameters
    screen,  # Surface to place button on
    WIDTH - 110,  # X-coordinate of top left corner
    140,  # Y-coordinate of top left corner
    100,  # Width
    30,  # Height

    # Optional Parameters
    text='Increase speed',  # Text to display
    fontSize=20,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(204, 229, 255),  # Colour of button when not being interacted with
    hoverColour=(204, 204, 255),  # Colour of button when being hovered over
    pressedColour=(102, 178, 255),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: myFunction4(final_list)  # Function to call when clicked on
)
button4 = Button(
# Mandatory Parameters
    screen,  # Surface to place button on
    WIDTH - 110,  # X-coordinate of top left corner
    180,  # Y-coordinate of top left corner
    100,  # Width
    30,  # Height

    # Optional Parameters
    text='Decrease speed',  # Text to display
    fontSize=20,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(204, 229, 255),  # Colour of button when not being interacted with
    hoverColour=(204, 204, 255),  # Colour of button when being hovered over
    pressedColour=(102, 178, 255),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: myFunction5(final_list)  # Function to call when clicked on
)
button5 = Button(
# Mandatory Parameters
    screen,  # Surface to place button on
    WIDTH - 110,  # X-coordinate of top left corner
    220,  # Y-coordinate of top left corner
    100,  # Width
    30,  # Height

    # Optional Parameters
    text='Rock to play',  # Text to display
    fontSize=20,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(204, 229, 255),  # Colour of button when not being interacted with
    hoverColour=(204, 204, 255),  # Colour of button when being hovered over
    pressedColour=(102, 178, 255),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: myFunction6(final_list)  # Function to call when clicked on
)
button6 = Button(
# Mandatory Parameters
    screen,  # Surface to place button on
    WIDTH - 110,  # X-coordinate of top left corner
    260,  # Y-coordinate of top left corner
    100,  # Width
    30,  # Height

    # Optional Parameters
    text='Paper to play',  # Text to display
    fontSize=20,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(204, 229, 255),  # Colour of button when not being interacted with
    hoverColour=(204, 204, 255),  # Colour of button when being hovered over
    pressedColour=(102, 178, 255),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: myFunction7(final_list)  # Function to call when clicked on
)
button7 = Button(
# Mandatory Parameters
    screen,  # Surface to place button on
    WIDTH - 110,  # X-coordinate of top left corner
    300,  # Y-coordinate of top left corner
    100,  # Width
    30,  # Height

    # Optional Parameters
    text='Scissors to play',  # Text to display
    fontSize=20,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(204, 229, 255),  # Colour of button when not being interacted with
    hoverColour=(204, 204, 255),  # Colour of button when being hovered over
    pressedColour=(102, 178, 255),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: myFunction8(final_list)  # Function to call when clicked on
)

def myFunction1(final_list):
    x = random.randint(IMG_WIDTH, (WIDTH - IMG_WIDTH))
    y = random.randint(IMG_HEIGHT, (HEIGHT - IMG_HEIGHT))

    item = Object((x, y), ROCK_IMG, 0, 'rock')
    item.speed = standard_speed
    item.angle = random.uniform(0, math.pi * 2)

    final_list.append(item)

def myFunction2(final_list):
    x = random.randint(IMG_WIDTH, (WIDTH - IMG_WIDTH))
    y = random.randint(IMG_HEIGHT, (HEIGHT - IMG_HEIGHT))

    item = Object((x, y), PAPER_IMG, 0, 'paper')
    item.speed = standard_speed
    item.angle = random.uniform(0, math.pi * 2)

    final_list.append(item)

def myFunction3(final_list):
    x = random.randint(IMG_WIDTH, (WIDTH - IMG_WIDTH))
    y = random.randint(IMG_HEIGHT, (HEIGHT - IMG_HEIGHT))

    item = Object((x, y), SCISSORS_IMG, 0, 'scissors')
    item.speed = standard_speed
    item.angle = random.uniform(0, math.pi * 2)

    final_list.append(item)

def myFunction4(final_list):
    global standard_speed
    standard_speed += 0.05
    for i in final_list:
        i.speed += 0.05

def myFunction5(final_list):
    global standard_speed
    if standard_speed != 0:
        standard_speed -= 0.05
    for i in final_list:
        if i.speed != 0:
            i.speed -= 0.05
# make collide function for irregular objects

def myFunction6(final_list):
    x = random.randint(IMG_WIDTH, (WIDTH - IMG_WIDTH))
    y = random.randint(IMG_HEIGHT, (HEIGHT - IMG_HEIGHT))

    item = Object((x, y), C_ROCK_IMG, 1, 'rock')
    item.speed = standard_speed
    item.angle = random.uniform(0, math.pi * 2)

    final_list.append(item)
    button5.hide()
    button6.hide()
    button7.hide()

def myFunction7(final_list):
    x = random.randint(IMG_WIDTH, (WIDTH - IMG_WIDTH))
    y = random.randint(IMG_HEIGHT, (HEIGHT - IMG_HEIGHT))

    item = Object((x, y), C_PAPER_IMG, 1, 'paper')
    item.speed = standard_speed
    item.angle = random.uniform(0, math.pi * 2)

    final_list.append(item)
    button5.hide()
    button6.hide()
    button7.hide()

def myFunction8(final_list):
    x = random.randint(IMG_WIDTH, (WIDTH - IMG_WIDTH))
    y = random.randint(IMG_HEIGHT, (HEIGHT - IMG_HEIGHT))

    item = Object((x, y), C_SCISSORS_IMG, 1, 'scissors')
    item.speed = standard_speed
    item.angle = random.uniform(0, math.pi * 2)

    final_list.append(item)
    button5.hide()
    button6.hide()
    button7.hide()

def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    dist = math.hypot(dx, dy)

    if p1.type == p2.type:
        pass

    elif dist < IMG_WIDTH:
        tangent = math.atan2(dy, dx)
        angle = 0.5 * math.pi + tangent

        angle1 = 2 * tangent - p1.angle
        angle2 = 2 * tangent - p2.angle
        speed1 = p2.speed
        speed2 = p1.speed

        (p1.angle, p1.speed) = (angle1, speed1)
        (p2.angle, p2.speed) = (angle2, speed2)

        p1.x += math.sin(angle)
        p1.y -= math.cos(angle)
        p2.x -= math.sin(angle)
        p2.y += math.cos(angle)

        if p1.filename == ROCK_IMG and p2.filename == SCISSORS_IMG:
            setattr(p2, 'filename', ROCK_IMG)
            setattr(p2, 'image', (pygame.transform.scale(pygame.image.load(ROCK_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p2, 'type', 'rock')

        if p1.filename == SCISSORS_IMG and p2.filename == ROCK_IMG:
            setattr(p1, 'filename', ROCK_IMG)
            setattr(p1, 'image', (pygame.transform.scale(pygame.image.load(ROCK_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p2, 'type', 'rock')

        if p1.filename == ROCK_IMG and p2.filename == PAPER_IMG:
            setattr(p1, 'filename', PAPER_IMG)
            setattr(p1, 'image', (pygame.transform.scale(pygame.image.load(PAPER_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p1, 'type', 'paper')

        if p1.filename == PAPER_IMG and p2.filename == ROCK_IMG:
            setattr(p2, 'filename', PAPER_IMG)
            setattr(p2, 'image', (pygame.transform.scale(pygame.image.load(PAPER_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p2, 'type', 'paper')

        if p1.filename == PAPER_IMG and p2.filename == SCISSORS_IMG:
            setattr(p1, 'filename', SCISSORS_IMG)
            setattr(p1, 'image', (pygame.transform.scale(pygame.image.load(SCISSORS_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p1, 'type', 'scissors')

        if p1.filename == SCISSORS_IMG and p2.filename == PAPER_IMG:
            setattr(p2, 'filename', SCISSORS_IMG)
            setattr(p2, 'image', (pygame.transform.scale(pygame.image.load(SCISSORS_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p2, 'type', 'scissors')


        if p1.filename == C_ROCK_IMG and p2.filename == SCISSORS_IMG:
            setattr(p2, 'filename', ROCK_IMG)
            setattr(p2, 'image', (pygame.transform.scale(pygame.image.load(ROCK_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p2, 'type', 'rock')

        if p1.filename == C_SCISSORS_IMG and p2.filename == ROCK_IMG:
            setattr(p1, 'filename', C_ROCK_IMG)
            setattr(p1, 'image', (pygame.transform.scale(pygame.image.load(C_ROCK_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p1, 'type', 'rock')

        if p1.filename == C_ROCK_IMG and p2.filename == PAPER_IMG:
            setattr(p1, 'filename', C_PAPER_IMG)
            setattr(p1, 'image', (pygame.transform.scale(pygame.image.load(C_PAPER_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p1, 'type', 'paper')

        if p1.filename == C_PAPER_IMG and p2.filename == ROCK_IMG:
            setattr(p2, 'filename', PAPER_IMG)
            setattr(p2, 'image', (pygame.transform.scale(pygame.image.load(PAPER_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p2, 'type', 'paper')

        if p1.filename == C_PAPER_IMG and p2.filename == SCISSORS_IMG:
            setattr(p1, 'filename', C_SCISSORS_IMG)
            setattr(p1, 'image', (pygame.transform.scale(pygame.image.load(C_SCISSORS_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p1, 'type', 'scissors')

        if p1.filename == C_SCISSORS_IMG and p2.filename == PAPER_IMG:
            setattr(p2, 'filename', SCISSORS_IMG)
            setattr(p2, 'image', (pygame.transform.scale(pygame.image.load(SCISSORS_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p2, 'type', 'scissors')


        if p2.filename == C_ROCK_IMG and p1.filename == SCISSORS_IMG:
            setattr(p1, 'filename', ROCK_IMG)
            setattr(p1, 'image', (pygame.transform.scale(pygame.image.load(ROCK_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p1, 'type', 'rock')

        if p2.filename == C_SCISSORS_IMG and p1.filename == ROCK_IMG:
            setattr(p2, 'filename', C_ROCK_IMG)
            setattr(p2, 'image', (pygame.transform.scale(pygame.image.load(C_ROCK_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p2, 'type', 'rock')

        if p2.filename == C_ROCK_IMG and p1.filename == PAPER_IMG:
            setattr(p2, 'filename', C_PAPER_IMG)
            setattr(p2, 'image', (pygame.transform.scale(pygame.image.load(C_PAPER_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p2, 'type', 'paper')

        if p2.filename == C_PAPER_IMG and p1.filename == ROCK_IMG:
            setattr(p1, 'filename', PAPER_IMG)
            setattr(p1, 'image', (pygame.transform.scale(pygame.image.load(PAPER_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p1, 'type', 'paper')

        if p2.filename == C_PAPER_IMG and p1.filename == SCISSORS_IMG:
            setattr(p2, 'filename', C_SCISSORS_IMG)
            setattr(p2, 'image', (pygame.transform.scale(pygame.image.load(C_SCISSORS_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p2, 'type', 'scissors')

        if p2.filename == C_SCISSORS_IMG and p1.filename == PAPER_IMG:
            setattr(p1, 'filename', SCISSORS_IMG)
            setattr(p1, 'image', (pygame.transform.scale(pygame.image.load(SCISSORS_IMG), (IMG_WIDTH, IMG_HEIGHT))))
            setattr(p1, 'type', 'scissors')
class Object:
    def __init__(self, position, filename, control, type):
        self.x, self.y = position
        self.filename = filename
        self.speed = 0
        self.angle = 0
        self.image = pygame.transform.scale(pygame.image.load(filename), (IMG_WIDTH, IMG_HEIGHT))
        self.is_controlled = control
        self.type = type

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, final_list):
        if self.type == 'scissors':
            dist_p = 1000000
            dist_r = 1000000
            dist_s = 1000000
            count_s = 0
            count_p = 0
            count_r = 0
            cl_pap = Object
            cl_rock = Object
            for i in final_list:
                dx = numpy.array([self.x, self.y], float)
                dy = numpy.array([i.x, i.y], float)
                if i.type == 'paper':
                    if dist_p > numpy.linalg.norm(dx - dy):
                        dist_p = numpy.linalg.norm(dx - dy)
                        count_p += 1
                        cl_pap = i

                if i.type == 'rock':
                    if dist_r > numpy.linalg.norm(dx - dy):
                        dist_r = numpy.linalg.norm(dx - dy)
                        count_r += 1
                        cl_rock = i

                if i.type == 'scissors':
                    if dist_s > numpy.linalg.norm(dx - dy):
                        dist_s = numpy.linalg.norm(dx - dy)
                        count_s += 1
            if self.is_controlled == 0:
                if dist_r < 200:
                    self.run_away(cl_rock)

                elif dist_p < 500:
                    self.move_towards(cl_pap)

                else:
                    self.x += math.cos(self.angle) * self.speed
                    self.y += math.sin(self.angle) * self.speed
            self.teleport()


        if self.type == 'rock':
            dist_p = 1000000
            dist_s = 1000000
            dist_r = 1000000
            count_s = 0
            count_p = 0
            count_r = 0
            cl_s = Object
            cl_pap = Object
            for i in final_list:
                dx = numpy.array([self.x, self.y], float)
                dy = numpy.array([i.x, i.y], float)
                if i.type == 'paper':
                    if dist_p > numpy.linalg.norm(dx - dy):
                        dist_p = numpy.linalg.norm(dx - dy)
                        count_p += 1
                        cl_pap = i

                if i.type == 'rock':
                    if dist_r > numpy.linalg.norm(dx - dy):
                        dist_r = numpy.linalg.norm(dx - dy)
                        count_r += 1

                if i.type == 'scissors':
                    if dist_s > numpy.linalg.norm(dx - dy) < 100:
                        dist_s = numpy.linalg.norm(dx - dy)
                        count_s += 1
                        cl_s = i
            if self.is_controlled == 0:
                if dist_p < 200:
                    self.run_away(cl_pap)
                elif dist_s < 500:
                    self.move_towards(cl_s)
                else:
                    self.x += math.cos(self.angle) * self.speed
                    self.y += math.sin(self.angle) * self.speed
            self.teleport()

        if self.type == 'paper':
            dist_r = 1000000
            dist_s = 1000000
            dist_p = 1000000
            count_s = 0
            count_p = 0
            count_r = 0
            cl_r = Object
            cl_s = final_list[0]
            for i in final_list:
                dx = numpy.array([self.x, self.y], float)
                dy = numpy.array([i.x, i.y], float)
                if i.filename == 'paper':
                    if dist_p > numpy.linalg.norm(dx - dy):
                        dist_p = numpy.linalg.norm(dx - dy)
                        count_p += 1

                if i.filename == 'rock':
                    if dist_r > numpy.linalg.norm(dx - dy):
                        dist_r = numpy.linalg.norm(dx - dy)
                        count_r += 1
                        cl_r = i

                if i.filename == 'scissors':
                    dist_s = min(dist_s, numpy.linalg.norm(dx - dy))
                    if dist_s > numpy.linalg.norm(dx - dy):
                        dist_s = numpy.linalg.norm(dx - dy)
                        count_s += 1
                        cl_s = i
            if self.is_controlled == 0:
                if dist_s < 200:
                    self.run_away(cl_s)
                elif dist_r < 500:
                    self.move_towards(cl_r)
                else:
                    self.x += math.cos(self.angle) * self.speed
                    self.y += math.sin(self.angle) * self.speed
            self.teleport()

    def teleport(self):
        if self.x >= WIDTH:
            self.x = IMG_WIDTH

        # right wall
        elif self.x < 0:
            self.x = WIDTH - IMG_WIDTH

        # floor
        if self.y >= HEIGHT:
            self.y = IMG_HEIGHT

        # ceiling
        elif self.y < 0:
            self.y = HEIGHT - IMG_HEIGHT

    def move_towards(self, target):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = target.x - self.x, target.y - self.y
        dist = math.hypot(dx, dy) + 50
        dx, dy = dx / dist, dy / dist  # Normalize.
        self.x += dx * (self.speed)
        self.y += dy * (self.speed)

    def run_away(self, target):
        dx, dy = target.x - self.x, target.y - self.y
        dist = math.hypot(dx, dy)
        if dist == 0:
            return
        dx, dy = dx / dist, dy / dist  # Normalize.
        self.x -= dx * self.speed
        self.y -= dy * self.speed



final_list = []

rock_count = 1

for n in range(rock_count):
    x = random.randint(IMG_WIDTH, (WIDTH - IMG_WIDTH))
    y = random.randint(IMG_HEIGHT, (HEIGHT - IMG_HEIGHT))

    item = Object((x, y), ROCK_IMG, 0, 'rock')
    item.speed = standard_speed
    item.angle = random.uniform(0, math.pi * 2)

    final_list.append(item)

paper_count = 1
for n in range(paper_count):
    x = random.randint(IMG_WIDTH, (WIDTH - IMG_WIDTH))
    y = random.randint(IMG_HEIGHT, (HEIGHT - IMG_HEIGHT))

    item = Object((x, y), PAPER_IMG, 0, 'paper')
    item.speed = standard_speed
    item.angle = random.uniform(0, math.pi * 2)
    final_list.append(item)

scissors_count = 1

for n in range(scissors_count):
    x = random.randint(IMG_WIDTH, (WIDTH - IMG_WIDTH))
    y = random.randint(IMG_HEIGHT, (HEIGHT - IMG_HEIGHT))

    scissors = Object((x, y), SCISSORS_IMG, 0, 'scissors')
    scissors.speed = standard_speed
    scissors.angle = random.uniform(0, math.pi * 2)

    final_list.append(scissors)

running = True

while running:
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and count == 1:  # Move up
        selected_item.y -= standard_speed
    if keys[pygame.K_s] and count == 1:  # Move down
        selected_item.y += standard_speed
    if keys[pygame.K_a] and count == 1:  # Move left
        selected_item.x -= standard_speed
    if keys[pygame.K_d] and count == 1:  # Move right
        selected_item.x += standard_speed
    for event in events:
        count = 0
        for i in final_list:
            if i.is_controlled == 1:
                count += 1
                selected_item = i
        if count > 1:
            running = False
        if event.type == pygame.QUIT:
            running = False
        t = final_list[0].type
        flag = 1
        for i in final_list:
            if i.type != t:
                flag = 0
        if flag:
            running = False


    screen.fill(BG_COLOR)

    for i, item in enumerate(final_list):
        item.move(final_list)

        for item_two in final_list[i + 1:]:
            collide(item, item_two)
        item.display(screen)

    pygame_widgets.update(events)
    pygame.display.flip()



