import moderngl as mgl
import numpy as np
import glm


class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.vao_name = vao_name
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, self.pos)
        # rotate
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        # scale
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vao.render()


class ExtendedBaseModel(BaseModel):
    def __init__(self, app, vao_name, tex_id, pos, rot, scale):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use(location=0)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def update_shadow(self):
        self.shadow_program['m_model'].write(self.m_model)

    def render_shadow(self):
        self.update_shadow()
        self.shadow_vao.render()

    def on_init(self):
        self.program['m_view_light'].write(self.app.light.m_view_light)
        # resolution
        self.program['u_resolution'].write(glm.vec2(self.app.WIN_SIZE))
        # depth texture
        self.depth_texture = self.app.mesh.texture.textures['depth_texture']
        self.program['shadowMap'] = 1
        self.depth_texture.use(location=1)
        # shadow
        self.shadow_vao = self.app.mesh.vao.vaos['shadow_' + self.vao_name]
        self.shadow_program = self.shadow_vao.program
        self.shadow_program['m_proj'].write(self.camera.m_proj)
        self.shadow_program['m_view_light'].write(self.app.light.m_view_light)
        self.shadow_program['m_model'].write(self.m_model)
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use(location=0)
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)


class Cube(ExtendedBaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class Deer(ExtendedBaseModel):
    def __init__(self, app, vao_name='deer', tex_id='deer',
                 pos=(0, 10, 0), rot=(-90, 0, 0), scale=(0.05, 0.05, 0.05)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class BigDeer(ExtendedBaseModel):
    def __init__(self, app, vao_name='deer', tex_id='deer',
                 pos=(0, 10, 0), rot=(-90, 180, 0), scale=(0.07, 0.07, 0.07)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Tapir(ExtendedBaseModel):
    def __init__(self, app, vao_name='tapir', tex_id='tapir',
                 pos=(0, 10, 0), rot=(-90, 180, 0), scale=(0.06, 0.06, 0.06)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class Ibex(ExtendedBaseModel):
    def __init__(self, app, vao_name='ibex', tex_id='ibex',
                 pos=(0, 10, 0), rot=(-90, 0, 0), scale=(0.06, 0.06, 0.06)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class Tree(ExtendedBaseModel):
    def __init__(self, app, vao_name='tree', tex_id='tree',
                 pos=(0, 10, 0), rot=(-90, 0, 0), scale=(0.02, 0.02, 0.02)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)




class Llama(ExtendedBaseModel):
    def __init__(self, app, vao_name='llama', tex_id='llama',
                 pos=(0, 10, 0), rot=(0, 90, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class BigLlama(ExtendedBaseModel):
    def __init__(self, app, vao_name='llama', tex_id='llama',
                 pos=(0, 10, 0), rot=(0, 270, 0), scale=(2, 2, 2)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Monkey(ExtendedBaseModel):
    def __init__(self, app, vao_name='monkey', tex_id='monkey',
                 pos=(0, 10, 0), rot=(-90, 0, 0), scale=(0.01, 0.01, 0.01)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
     
class BigMonkey(ExtendedBaseModel):
    def __init__(self, app, vao_name='monkey', tex_id='monkey',
                 pos=(0, 10, 0), rot=(-90, 0, 0), scale=(0.014, 0.014, 0.014)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Gate(ExtendedBaseModel):
    def __init__(self, app, vao_name='gate', tex_id='gate',
                 pos=(0, 0, 0), rot=(0, 90, 0), scale=(0.06, 0.06, 0.06)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class Wall(ExtendedBaseModel):
    def __init__(self, app, vao_name='wall', tex_id='wall',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(0.02, 0.02, 0.02)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class WallRotate(ExtendedBaseModel):
    def __init__(self, app, vao_name='wall', tex_id='wall',
                 pos=(0, 0, 0), rot=(-90, 90, 0), scale=(0.02, 0.02, 0.02)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Fence(ExtendedBaseModel):
    def __init__(self, app, vao_name='fence', tex_id='fence',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class BigFence(ExtendedBaseModel):
    def __init__(self, app, vao_name='fence', tex_id='fence',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(2, 2, 2)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class FenceRotate(ExtendedBaseModel):
    def __init__(self, app, vao_name='fence', tex_id='fence',
            pos=(0, 0, 0), rot=(0, 90, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#   SkyBox Model
class SkyBox(BaseModel):
    def __init__(self, app, vao_name='skybox', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0    # variable uniform name defined in frag shader
        self.texture.use(location=0)
        # mvp
        # Pass projection matrix to shader
        self.program['m_proj'].write(self.camera.m_proj)
        # Skybox wont move
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))





















