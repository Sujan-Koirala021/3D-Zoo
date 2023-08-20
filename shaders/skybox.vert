#version 330 core

// Vertex Shader for SkyBox

// Input vertex position
layout (location = 0) in vec3 in_position;

// Output texture coordinates for cube mapping
out vec3 texCubeCoords;

// Projection and view matrices
uniform mat4 m_proj;
uniform mat4 m_view;

void main() {
    // Assign vertex position to texture coordinates
    texCubeCoords = in_position;

    // Apply transformations
    vec4 pos = m_proj * m_view * vec4(in_position, 1.0);

    // Set final vertex position
    gl_Position = pos.xyww;
    gl_Position.z -= 0.0001; // Adjust for depth sorting and avoid depth conflict for near obj
}
