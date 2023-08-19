#   Intensity assignment to Ambient, Diffuse and Specular

import glm

#   Light Source
lightPos = (50, 50, -10)
lightColor = (1,1,1) # white light

class Light:
    def __init__(self, position=lightPos, color=lightColor):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(0, 0, 0)
        # intensities
        self.Ia = 0.06 * self.color  # ambient
        self.Id = 0.8 * self.color  # diffuse
        self.Is = 1.0 * self.color  # specular
        # view matrix
        self.m_view_light = self.get_view_matrix()

    def get_view_matrix(self):
        # lightPos, direcn , up vec
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))