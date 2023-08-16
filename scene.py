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

        # deer
        add(Deer(app, pos=(-15, -1, -4)))
        
        # wall
        add(Wall(app, pos=(25, -1, -10)))
        # gate
        add(Gate(app, pos = (31.5, -1, -10)))

        for xposition in range(0,30,6):
            add(Fence(app, pos=(-16+xposition, -1, -13)))
            # add(Fence(app, pos=(-16+xposition, -1, -7)))

        for yposition in range(0,30,12):
            add(Fence(app, pos=(-16, -1, -7+yposition)))

        for ypositionRot in range(0,30,6):
            add(FenceRotate(app, pos=(-13, -1, -10+ypositionRot)))
            add(FenceRotate(app, pos=(-19, -1, -10+ypositionRot)))

        #tree
        # add(Tree(app, pos=(-16, -1, 0)))
        # add((app, pos=(-15, -1, -4)))
        # # moving cube
        # self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        # add(self.moving_cube)

    # def update(self):
    #     self.moving_cube.rot.xyz = self.app.time
