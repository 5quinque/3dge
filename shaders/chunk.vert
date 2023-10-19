#version 330 core

layout (location = 0) in vec3 in_position;
layout (location = 1) in int voxel_id;
layout (location = 2) in int face_id;
layout (location = 3) in int ao_id;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;

out vec3 voxel_color;
out vec2 uv;
out float shading;

const float ao_values[4] = float[4](
    0.1, 0.25, 0.5, 1.0
);

const float face_shading[6] = float[6](
    1.0, 0.5,  // top bottom
    0.5, 0.8,  // right left
    0.5, 0.8   // front back
);

const vec2 uv_coords[4] = vec2[4](
    vec2(0.0, 0.0),
    vec2(0.0, 1.0),
    vec2(1.0, 0.0),
    vec2(1.0, 1.0)
);

const int uv_indices[12] = int[12](
    1, 0, 2, 1, 2, 3, // tex coords indices for vertices of an even face
    3, 0, 2, 3, 1, 0  // odd face
);

vec3 hash31(float p)
{
    vec3 p3 = fract(vec3(p * 21.2) * vec3(0.1031, 0.1030, 0.0973));
    p3 += dot(p3, p3.yzx + 33.33);
    return fract((p3.xxy + p3.yzz) * p3.zyx) + 0.05;
}


// function to return a color modifier based on the position of the voxel_color
// we want north facing voxels to be a different color than south facing voxels
// e.g. a shadow for dark voxels and a highlight for light voxels
vec3 get_color_modifier(vec3 position, int uv_index)
{
    vec3 color_modifier;

    // determine if we are on an even or odd face
    // if we are on an even face, we want to return a shadow color
    int face = uv_index / 6;
    if (face % 2 == 0)
    {
        // we are on an even face
        color_modifier = vec3(0.55, 0.55, 0.55);
    }
    else
    {
        // we are on an odd face
        color_modifier = vec3(1.5, 1.5, 1.5);
    }


    // 0.0195 is 5 / 256, and is the step size we're using for the color modifier
    // based on the height of the voxel
    color_modifier *= 0.0195 * position.y;

    return color_modifier;
}





void main()
{
    int uv_index = gl_VertexID % 6 + (face_id & 1) * 6;
    uv = uv_coords[uv_indices[uv_index]];
    // voxel_color = hash31(float(voxel_id));
    voxel_color = get_color_modifier(in_position, uv_index);
    shading = face_shading[face_id] * ao_values[ao_id];
    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
}
