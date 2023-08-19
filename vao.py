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
        

        # llama vao
        self.vaos['llama'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['llama'])

        # shadow llama vao
        self.vaos['shadow_llama'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['llama'])
        

        # tapir vao
        self.vaos['tapir'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['tapir'])

        # shadow tapir vao
        self.vaos['shadow_tapir'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['tapir'])


        # tree vao
        self.vaos['tree'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['tree'])

        # shadow tapir vao
        self.vaos['shadow_tree'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['tree'])


        # ibex vao
        self.vaos['ibex'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['ibex'])

        # shadow ibex vao
        self.vaos['shadow_ibex'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['ibex'])

               # monkey vao
        self.vaos['monkey'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['monkey'])

        # shadow monkey vao
        self.vaos['shadow_monkey'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['monkey'])
        
        
        # wall vao
        self.vaos['wall'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['wall'])

        # shadow wall vao
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


    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()