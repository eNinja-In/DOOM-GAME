import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self,game):
        self.game = game
        self.Screen = game.screen
        self.wall_testure = self.load_wall_testure()
        self.sky_image = self.get_texture("Resource/sky.jpg")
        self.sky_offset = 0

    def draw(self):
        # self.draw_background()
        self.render_game_object()

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.angle) % WIDTH
        self.Screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.Screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))

        pg.draw.rect(self.Screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))    
    def render_game_object(self):
        list_object = sorted(self.game.raycasting.object_to_renderer, key = lambda t: t[0], reverse = True)
        for depth, imag, pos in list_object:
            self.Screen.blit(imag, pos)

    @staticmethod
    def get_texture(path,res=(TEXTURE_SIZE,TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_testure(self):
        return {
            1:self.get_texture("Resource/1.jpg"),
            2:self.get_texture("Resource/2.jpg"),
            3:self.get_texture("Resource/3.jpg")
        }