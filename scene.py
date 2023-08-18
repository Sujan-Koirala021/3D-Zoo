from model import *
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # floor
        n, s = 40, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        # # columns
        # for i in range(9):
        #     add(Cube(app, pos=(15, i * s, -9 + i), tex_id=2))
        #     add(Cube(app, pos=(15, i * s, 5 - i), tex_id=2))

        
        # wall
        # for i in range(-30,30,2):
        for xposition in range(0,45,6):
            add(Wall(app, pos=(-25+xposition, -1, -27)))
            add(Wall(app, pos=(-25+xposition, -1, 27)))

        for ypositionRot in range(0,50,6):
            add(WallRotate(app, pos=(-28, -1, -24+ypositionRot)))
            if(ypositionRot!=24):
                add(WallRotate(app, pos=(-28+48, -1, -24+ypositionRot)))
            else:
                # gate
                add(Gate(app, pos = (-28+48, -1, -24.5+ypositionRot)))


        for xposition in range(0,36,6):
          add(Fence(app, pos=(-14+xposition, -1, -18)))
          add(Fence(app, pos=(-14+xposition, -1, -18+37)))

        for ypositionRot in range(0,50,6):
            add(FenceRotate(app, pos=(-17, -1,-24+ypositionRot)))

        add(FenceRotate(app, pos=(0, -1,-23+ypositionRot)))
        add(FenceRotate(app, pos=(0, -1,-21)))

        # deer

        add(Deer(app, pos=(-10, -1, 21)))
        add(BigDeer(app, pos=(-6, -1, 21)))

        #Llama
        add(Llama(app, pos=(6, -1.15, 21)))
        add(BigLlama(app, pos=(10, -1.15, 21)))
        #Tapir
        add(Tapir(app, pos=(-20, -1.15, 10)))
        add(Tapir(app, pos=(-21, -1.15, -7)))
        #Tree
        add(Tree(app, pos=(-20, -1.15, -20)))
        add(Tree(app, pos=(-20, -1.15, 0)))
        add(Tree(app, pos=(-20, -1.15, 20)))
        # monkey
        add(Monkey(app, pos=(-8, -1, -21)))
        add(BigMonkey(app, pos=(-4, -1, -21)))
        add(Tree(app, pos=(-11, -1, -21)))

        #Ibex
        add(Ibex(app, pos=(6, -1.15, -21)))
        # # moving cube
        # self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        # add(self.moving_cube)

    # def update(self):
    #     self.moving_cube.rot.xyz = self.app.time
