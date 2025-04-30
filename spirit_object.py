import pygame as pg
from settings import *

class SpiritObject:
    def __init__(self, game, path="Resource\spirit.png", pos=(2, 3.5), scale = 0.5, shift = 0.27):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDHT = self.image.get_width()
        self.IMAGE_HALF_WIDHT = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDHT / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.spirit_half_width = 0  
        self.SCALE_SPIRIT = scale
        self.SHIFT_SPIRIT_HEIGHT =shift

    def get_spirit_projection(self):
        proj = SCREEN_DIST / self.norm_dist * self.SCALE_SPIRIT
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj
        image = pg.transform.scale(self.image, (proj_width, proj_height))
        self.spirit_half_width = proj_width // 2
        height_shift = proj_height  * self.SHIFT_SPIRIT_HEIGHT
        pos = self.screen_x - self.spirit_half_width, HALF_HEIGHT - proj_height // 2 + height_shift

        self.game.raycasting.object_to_renderer.append((self.norm_dist, image, pos))
    
    def get_spirit(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y 
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle

        if (dx > 0 and self.player.angle > math.pi) or (dx< 0  and dy < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDHT < self.screen_x <(WIDTH + self.IMAGE_HALF_WIDHT) and self.norm_dist > 0.5:
            self.get_spirit_projection()


    def update(self):
        self.get_spirit()
