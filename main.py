import pygame as pg
import sys
from settings import *
from map import *
from player import * 
from raycasting import *
from object_renderer import *
from spirit_object import *


class Game:

    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen=pg.display.set_mode(RES)
        self.clock=pg.time.Clock()
        self.new_game()
        self.delta_time=1


    def new_game(self):
        self.map=Map(self)
        self.player=Player(self)
        self.object_rendrer = ObjectRenderer(self)
        self.raycasting=RayCasting(self)
        self.spirit = SpiritObject(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.spirit.update()
        pg.display.flip()
        self.delta_time=self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps() : .1f}")


    def draw(self):
        self.screen.fill("black")#background color
        self.object_rendrer.draw()
        # self.map.draw()
        # self.player.draw()


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
                pg.quit()
                sys.exit()


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game=Game()
    game.run()