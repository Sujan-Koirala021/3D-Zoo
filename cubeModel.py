import numpy as np

class Cube:
    def __init__(self, app):
        """
        Initializes a Triangle object.

        Parameters:
            app (object): An object containing an OpenGL context (ctx) provided by ModernGL.
        """
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.getVertexBufObj()
        self.shaderProgram = self.getShaderProgram('default')
        self.vao = self.getVertexArrayObject()
        self.onInit()
        
    def onInit(self):
        self.shaderProgram['m_proj'].write(self.app.camera.m_proj)

    def render(self):
        """
        Renders the triangle by calling the render method of the vertex array object (vao).
        """
        self.vao.render()

    def destroy(self):
        """
        Releases the resources used by the triangle, including the vertex array object,
        shader program, and vertex buffer object (vbo).
        """
        self.vao.release()
        self.shaderProgram.release()
        self.vbo.release()

    def getVertexArrayObject(self):
        """
        Creates and returns a vertex array object (vao) which associates the vertex buffer object (vbo)
        with the shader program. It specifies the vertex attributes and their locations in the shader.

        Returns:
            moderngl.VertexArray: A vertex array object representing the triangle.
        """
        vao = self.ctx.vertex_array(self.shaderProgram, [(self.vbo, '3f', 'in_position')])
        return vao

    def getVertexData(self):
        """
        Returns a NumPy array containing the vertex positions of the cube.

        Returns:
            numpy.ndarray: A NumPy array with 3D vertex positions (x, y, z) for the cube.
        """
        # Define the 3D vertex positions for a cube with eight vertices
        # (x, y, z) coordinates for each vertex.
        vertices = [
            (-1, -1, 1),   # Front bottom left
            (1, -1, 1),    # Front bottom right
            (1, 1, 1),     # Front top right
            (-1, 1, 1),    # Front top left
            (-1, -1, -1),  # Back bottom left
            (1, -1, -1),   # Back bottom right
            (1,1 , -1),    # Back top right
            (-1, 1, -1)    # Back top left
        ]

        indices = [(0,2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2,7),
                   (0, 6, 1), (0, 5, 6)]
        
        vertexData = self.getData(vertices, indices)

        # vertexData = np.array(vertexData, dtype='f4')  # Numpy array with float32 data type
        return vertexData

    @staticmethod
    def getData(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype = 'f4')

    def getVertexBufObj(self):
        """
        Creates and returns a vertex buffer object (vbo) that stores the vertex data in the OpenGL buffer.

        Returns:
            moderngl.Buffer: A vertex buffer object representing the vertex data of the triangle.
        """
        vertexData = self.getVertexData()
        vbo = self.ctx.buffer(vertexData)
        return vbo

    def getShaderProgram(self, shaderName):
        """
        Loads and compiles vertex and fragment shader code from files and creates a shader program.

        Parameters:
            shaderName (str): The name of the shader program without the file extension.

        Returns:
            moderngl.Program: A shader program representing the rendering pipeline for the triangle.
        """
        with open(f'shaders/{shaderName}.vert') as file:
            vertexShader = file.read()

        with open(f'shaders/{shaderName}.frag') as file:
            fragmentShader = file.read()

        program = self.ctx.program(vertex_shader=vertexShader, fragment_shader=fragmentShader)
        return program
