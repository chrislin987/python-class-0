from pycat.core import Window, KeyCode, Scheduler
from pycat.sprite import Sprite
from pyglet.gl.glext_arb import PFNGLCLEARBUFFERFIPROC


window= Window(background_image="img/beach_03.png")

class Player(Sprite):
    def on_create(self):
        self.image='img/cat.png'
        self.x=50
        self.y=50
    
    def on_update(self, dt):

        if window.is_key_pressed(KeyCode.RIGHT):
            self.x += 100
            self.scale_x = 1

        if window.is_key_pressed(KeyCode.LEFT):
            self.x -= 100
            self.scale_x = -1



        


class Gem(Sprite):
    def on_create(self):
        self.image = 'img/gem_shiny04.png'
        self.goto_random_position()
        self.y = 700
        self.scale = 0.3
    
    def on_update(self, dt):
        self.y -= 100
        if self.is_touching_any_sprite():
            self.delete()
        if self.y < 0:
            self.delete()
    




def create_gem():
    window.create_sprite(Gem)
Scheduler.update(create_gem, 1)
window.create_sprite(Player)

window.run()