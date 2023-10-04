from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.image = load_image('ball21x21.png')
        self.drop_speed = random.randint(6, 15)

    def update(self):
        if self.y > 30 + 31:
            self.y -= self.drop_speed
        else:
            self.y = 30 + 31

    def draw(self):
        self.image.draw(self.x, self.y)


class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.image = load_image('ball41x41.png')
        self.drop_speed = random.randint(6, 15)

    def update(self):
        if self.y > 30 + 41:
            self.y -= self.drop_speed
        else:
            self.y = 30 + 41

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global world
    global small_ball
    global big_ball
    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team
    balls = random.randint(0, 20)
    small_ball = [SmallBall() for i in range(balls)]
    world += small_ball
    big_ball = [BigBall() for i in range(20-balls)]
    world += big_ball


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()  # game logic
    render_world()  # draw game world
    delay(0.05)
# finalization code


close_canvas()
