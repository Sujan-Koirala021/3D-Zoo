from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])

        # shadow cube vao
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cube'])

        # deer vao
        self.vaos['deer'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['deer'])

        # shadow deer vao
        self.vaos['shadow_deer'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['deer'])
        
               # monkey vao
        self.vaos['monkey'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['monkey'])

        # shadow deer vao
        self.vaos['shadow_monkey'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['monkey'])
        
        
        # wall vao
        self.vaos['wall'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['wall'])

        # shadow deer vao
        self.vaos['shadow_wall'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['wall'])
        
        
                # gate vao
        self.vaos['gate'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['gate'])

        # shadow gate vao
        self.vaos['shadow_gate'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['gate'])
        
                # fence vao
        self.vaos['fence'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['fence'])

        # shadow fence vao
        self.vaos['shadow_fence'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['fence'])
        

        # skybox vao
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])

        # advanced_skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(
            program=self.program.programs['advanced_skybox'],
            vbo=self.vbo.vbos['advanced_skybox'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()