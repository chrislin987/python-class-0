from os import spawnle
from pycat.core import Window                   




answer=input('please enter')
size=input('please enter')
Window = Window()
print('Hi', answer)
animal=Window.create_sprite()

if answer=='owl':
    animal.image='owl.gif'

if answer=='rat':
    animal.image='rat.png'

if size=='big':
    animal.scale=2
if size=='small':
    animal.scale=0.2
animal.y=300
animal.x=550
Window.run()