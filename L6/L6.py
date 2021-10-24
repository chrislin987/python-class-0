from pycat.base.base_sprite import RotationMode
from pycat.core import Window, KeyCode, Scheduler
from pycat.sprite import Sprite
from pyglet.window.key import D


window= Window(background_image="media/underwater_04.png")

class Spaceship(Sprite):
    def on_create(self):
        self.image='media/saucer.png'
        self.x=50
        self.y=500
        self.scale=0.3
        self.score=0
        self.rotation_mode = RotationMode.NO_ROTATION

    def on_update(self, dt):
        if self.is_touching_window_edge():
            self.rotation += 180
        self.move_forward(5)


class Alien(Sprite):
    def on_create(self):
        self.image='media/1.png'
        self.goto_random_position()
        self.y=60
        self.scale=0.2
        self.is_clicked=False

    def on_left_click(self):
        self.is_clicked=True
    def on_update(self, dt):
        if self.is_clicked:
            self.y +=10
            if self.is_touching_sprite(ship):
                self.delete()
                ship.score +=1
                label.text='score = '+str(ship.score)
            if self.is_touching_window_edge():
                self.delete()

def create_alien():
    window.create_sprite(Alien)


label=window.create_label()
label.text = 'Score = 0'







    
Scheduler.update(create_alien,0.3)

ship = window.create_sprite(Spaceship)
window.run()        