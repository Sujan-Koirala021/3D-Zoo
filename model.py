import numpy as np

class Triangle:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.getVertexBufObj()
        self.shaderProgram = self.getShaderProgram('default')
        self.vao = self.getVertexArrayObject()
    
    
    #   Render the model
    def render(self):
        self.vao.render()

    def destroy(self):
        self.vao.release()
        self.shaderProgram.release()
        self.vbo.release()

    
    def getVertexArrayObject(self):
        vao = self.ctx.vertex_array(self.shaderProgram, [(self.vbo, '3f', 'in_position')])
        return vao
    
    def getVertexData(self):
        vertexData = [(-0.6, -0.8, 0.0), (0.6, -0.8, 0.0), (0.0, 0.8, 0.0)]
        vertexData = np.array(vertexData, dtype = 'f4') # Numpy array with float 32 data type
        return vertexData
    
    def getVertexBufObj(self):
        vertexData = self.getVertexData()
        vbo = self.ctx.buffer(vertexData)
        return vbo
    
    def getShaderProgram(self,shaderName):
        with open(f'shaders/{shaderName}.vert') as file:
            vertexShader = file.read()
            
        with open(f'shaders/{shaderName}.frag') as file:
            fragmentShader = file.read()
            
        program = self.ctx.program(vertex_shader = vertexShader, fragment_shader = fragmentShader)
        return program