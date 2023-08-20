import pygame as pg
import moderngl as mgl
import glm


class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/img.jpg')
        self.textures[1] = self.get_texture(path='textures/img_1.png')
        self.textures[2] = self.get_texture(path='textures/img_2.png')
        self.textures['deer'] = self.get_texture(path='objects/deer/12961_White-TailedDeer_diffuse.jpg')
        self.textures['monkey'] = self.get_texture(path='objects/monkey/14092_ speak_No_ Evil_ Monkey_v2_diff.jpg')
        self.textures['llama'] = self.get_texture(path='objects/llama/llama04.jpg')
        self.textures['tapir'] = self.get_texture(path='objects/tapir/tapir_diffuse.jpg')
        self.textures['tree'] = self.get_texture(path='objects/tree/10447_Pine_Tree_v1_Diffuse.jpg')

        self.textures['ibex'] = self.get_texture(path='objects/ibex/13575_Ibex_diff.jpg')


        self.textures['fence'] = self.get_texture(path='objects/fence/Fence.png')
        self.textures['wall'] = self.get_texture(path='objects/wall/wall_diffuse.jpg')

        self.textures['gate'] = self.get_texture(path='objects/gate/textures/gate_diffuse.jpg')
        # self.textures['gate'] = self.get_texture(path='objects/gate/textures/pillar_diffuse.jpg')

        # self.textures['gate_normal'] = self.get_texture(path='objects/gate/textures/gate_normal.jpg')
        # self.textures['gate_specular'] = self.get_texture(path='objects/gate/textures/gate_specular.jpg')


        self.textures['skybox'] = self.get_texture_cube(dir_path='textures/skybox1/', ext='png')
        self.textures['depth_texture'] = self.get_depth_texture()

    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture(self.app.WIN_SIZE)
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture

    # Get Texture for Skybox
    def get_texture_cube(self, dir_path, ext='png'):
        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]
        # textures = [pg.image.load(dir_path + f'{face}.{ext}').convert() for face in faces]
        textures = []
        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)

        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            #   Convert texture to string data in rgb format and write to face
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,data=pg.image.tostring(texture, 'RGB'))
        # mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        # AF
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]