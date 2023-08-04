#version 330 core

// Input attribute: vertex position in 3D space
layout (location = 0) in vec3 in_position;

// Main vertex shader function
void main()
{
    // The vertex shader transforms the input vertex position into clip space.

    // gl_Position is a built-in output variable representing the transformed vertex position in clip space.
    // It is of type vec4, where the x, y, and z components represent the 3D position,
    // and the w component represents the perspective division factor.

    // Construct a 4D vector by using the in_position vector as the x, y, and z components,
    // and setting the w component to 1.0. The w component is crucial for perspective division.
    gl_Position = vec4(in_position, 1.0);
}
