#version 330 core

// Output variable: fragment color in RGBA format
layout (location = 0) out vec4 fragColor;

// Main fragment shader function
void main()
{
    // The fragment shader sets the color of the current fragment to green.

    // Create a 3D vector representing the color green.
    vec3 color = vec3(0, 1, 0); // (R=0, G=1, B=0)

    // Assign the color to the output fragment variable fragColor.
    // The vec4 constructor is used to create a 4D vector (RGBA),
    // where the x, y, and z components represent the RGB color values,
    // and the w component represents the alpha (transparency) value.
    fragColor = vec4(color, 1.0); // The alpha value is set to 1.0 (fully opaque).
}
