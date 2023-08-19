#   Navigate and View 3D scene

import glm
import pygame as pg

FOV = 50  # Field of View in degrees
NEAR = 0.1  # Near clipping plane
FAR = 100  # Far clipping plane
SPEED = 0.005  # Movement speed of the camera
SENSITIVITY = 0.04  # Mouse sensitivity for rotation

init_camera_pos = (39, 6, -0.2)

class Camera:
    def __init__(self, app, position=init_camera_pos, yaw=-180, pitch=0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)  # Camera position
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch

        # view matrix
        # the objects appear as if being viewed from the camera's perspective
        self.m_view = self.get_view_matrix()
        # projection matrix
        #  how objects in the real world appear smaller as they move farther away from the viewer. 
        self.m_proj = self.get_projection_matrix()

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel() # how much mouse moved till last frame
        self.yaw += rel_x * SENSITIVITY # camera turn left-right
        self.pitch -= rel_y * SENSITIVITY # camera turn up-down
        
        self.pitch = max(-89, min(89, self.pitch)) # prevent upside down/flipping camera

    # Recalculates the camera's direction vectors (forward, right, and up) based on the camera's current yaw and pitch angles.
    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward) # normalize -> vector length limit to 1
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        
        self.checkKeyEvent()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def checkKeyEvent(self):
        velocity = SPEED * self.app.delta_time
        #   Check for keyboard press for camera movement
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]: # move ahead
            self.position += self.forward * velocity
        if keys[pg.K_DOWN]: # move back
            self.position -= self.forward * velocity
        if keys[pg.K_LEFT]: # move left
            self.position -= self.right * velocity
        if keys[pg.K_RIGHT]: # move right
            self.position += self.right * velocity
        if keys[pg.K_a]:    #   move up
            self.position += self.up * velocity
        if keys[pg.K_z]:    # move down
            self.position -= self.up * velocity

    def get_view_matrix(self):
        # eye(cam pos), target we look at, up
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    #   Depict depth and perspective
    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)




















