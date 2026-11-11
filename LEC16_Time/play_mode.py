from pico2d import *
import game_world
import game_framework
from boy import Boy
from bird import Bird
from grass import Grass

boy = None
BIRD_COUNT = 10
BIRD_START_X = 100
BIRD_X_SPACING = 150
BIRD_START_Y = 300
BIRD_Y_VARIATION = 55


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    for index in range(BIRD_COUNT):
        bird = Bird(
            BIRD_START_X + index * BIRD_X_SPACING,
            BIRD_START_Y + (index % 4) * BIRD_Y_VARIATION,
        )
        game_world.add_oject(bird)

    grass = Grass()
    game_world.add_oject(grass, 0)


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()






