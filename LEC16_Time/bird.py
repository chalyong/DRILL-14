from pico2d import *


# bird flight speed
PIXEL_PER_METER = 10.0 / 0.3
FLY_SPEED_KMPH = 40.0
FLY_SPEED_MPS = FLY_SPEED_KMPH * 1000.0 / 3600.0
FLY_SPEED_PPS = FLY_SPEED_MPS * PIXEL_PER_METER

WINGBEAT_DISTANCE_M = 2.6
WINGBEAT_FRAMES = 14
FLY_FRAME_PER_SECOND = (
    FLY_SPEED_MPS / WINGBEAT_DISTANCE_M * WINGBEAT_FRAMES
)


class Bird:
    FRAME_WIDTH = 183
    FRAME_HEIGHT = 168
    FRAMES_PER_ROW = 5

    def __init__(self, x, y):
        self.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0.0
        self.dir = 1

    def update(self):
        self.frame = (
            self.frame + FLY_FRAME_PER_SECOND * game_framework.frame_time
        ) % WINGBEAT_FRAMES
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time

    def draw(self):
        frame = int(self.frame)
        row, column = divmod(frame, self.FRAMES_PER_ROW)
        self.image.clip_composite_draw(
            column * self.FRAME_WIDTH,
            (2 - row) * self.FRAME_HEIGHT,
            self.FRAME_WIDTH,
            self.FRAME_HEIGHT,
            0,
            '' if self.dir == 1 else 'h',
            self.x,
            self.y,
            self.FRAME_WIDTH,
            self.FRAME_HEIGHT,
        )
