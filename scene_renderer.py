

class SceneRenderer:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        self.scene = app.scene
        # depth buffer setup
        self.depth_texture = self.mesh.texture.textures['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    #   Rendering shadow maps
    def render_shadow(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.objects:
            obj.render_shadow()

    #   Rendering main scene    
    def main_render(self):
        self.app.ctx.screen.use()
        
        #   Render all objects in self.scene list
        for obj in self.scene.objects:
            obj.render()
        
        #   Render skybox
        self.scene.skybox.render()

    def render(self):
        # self.scene.update()
        # pass 1
        self.render_shadow()
        # pass 2
        self.main_render()

    def destroy(self):
        self.depth_fbo.release()

