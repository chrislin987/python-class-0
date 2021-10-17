
from pycat.core import Window, KeyCode
from pycat.sprite import Sprite



window = Window()





class Rat(Sprite):
    def on_create(self):
        self.scale=1
        self.image='rat.png'
        self.goto_random_position()

    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.I):
            self.y +=55
        if window.is_key_pressed(KeyCode.K):
            self.y -=55
        if window.is_key_pressed(KeyCode.L):
            self.x +=55
        if window.is_key_pressed(KeyCode.J):
            self.x -=55
        
        
for i in range(9):
    window.create_sprite(Rat)

class Fireball(Sprite):
    def on_create(self):
        self.scale=1
        self.image='fireball.gif'
        self.goto_random_position()
    def on_update(self, dt):
        

        if window.is_key_pressed(KeyCode.W):
            self.y +=55
        if window.is_key_pressed(KeyCode.S):
            self.y -=55
        if window.is_key_pressed(KeyCode.D):
            self.x +=55
        if window.is_key_pressed(KeyCode.A):
            self.x -=55





for i in range(99):
    window.create_sprite(Fireball)

window.run()