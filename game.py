from ursina import *
from random import randint
Entity(model='quad', scale=60, texture='phone.jpg')
app = Ursina()

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.parent = field
        self.model = "cube"
        self.color = color.black
        self.scale = .05
        self.position = (0, 0, -.03) 
        self.collider = 'box'
        self.dx = 0
        self.dy = 0
        self.eaten = 0

    def update(self):
        global body
        self.x += time.dt * self.dx
        self.y += time.dt * self.dy

        hit_info = self.intersects()

        if hit_info.hit:
            apple.x = randint(-4, 4) * .1
            apple.y = randint(-4, 4) * .1
            new_body=Entity(parent=field, model="cube", z=-.029,color=color.green, scale=.05)
            body.append(new_body)
        for i in range (len(body)-1, 0,-1):
            body[i].position=body[i-1].position
        if len(body)>0:
            body[0].x=self.x
            body[0].y=self.y
        if abs(self.x) > .47 or abs(self.y) > .47:
            for segment in body:
                segment.position=(10,10)
            print_on_screen("You Crashed!", position=(0, 0), origin=(0, 0), scale=2, duration=2)
            self.position = (0, 0)
            self.dx = 0   
            self.dy = 0 

    def input(self, key):
        if key == 'right arrow':
            self.dx = .3
            self.dy = 0
        if key == 'left arrow':
            self.dx = -.3
            self.dy = 0
        if key == 'up arrow':
            self.dx = 0
            self.dy = .3
        if key == 'down arrow':
            self.dx = 0
            self.dy = -.3



field_size = 19
field = Entity(model='quad', color=color.gray, scale=(12, 12), position=(field_size // 2, field_size // 2, -.01))

camera.position = (field_size // 2, -18, -18)
camera.rotation_x = -56

player = Player()
apple = Entity(parent=field, model="sphere", color=color.red, scale=.05, position=(.1, .1, -.03), collider='box')
body=[]
app.run()