
from pycat.core import Window
from pycat.sprite import Sprite



window = Window()





class Rat(Sprite):
    def on_create(self):
        self.scale=2.5
        self.image='rat.png'
        self.goto_random_position()
        
for i in range(50):
    window.create_sprite(Rat)

class Fireball(Sprite):
    def on_create(self):
        self.scale=2.5
        self.image='fireball.gif'
        self.goto_random_position()
        
for i in range(50):
    window.create_sprite(Fireball)



    




window.run()