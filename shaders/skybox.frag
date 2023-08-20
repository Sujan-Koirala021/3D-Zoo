#version 330 core
out vec4 fragColor;

// Holds texture coordinates (cube map coordinates)
in vec3 texCubeCoords;

// Sample  faces of cube based on 3D directions (vectors) 
uniform samplerCube u_texture_skybox;   // data from CPU

void main() {
    fragColor = texture(u_texture_skybox, texCubeCoords);
}