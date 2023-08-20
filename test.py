class Cube:
    def __init__(self, app):
        """
        Initializes a Cube object.
        Parameters:
            app (object): An object containing an OpenGL context (ctx) provided by ModernGL.
        """
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.getVertexBufObj()
        self.shaderProgram = self.getShaderProgram('default')
        self.vao = self.getVertexArrayObject()