#version 330

uniform mat4 projection;
uniform uint mode_id;

in vec2 in_vert;

out vec4 color;

const vec4 colors[2] = vec4[2](
    vec4(0.7, 0.1, 0.07, 0.75),
    vec4(0.1, 0.4, 7.0, 0.75)
);

void main() {
    gl_Position = projection * vec4(in_vert, 0.0, 1.0);
    color = colors[mode_id];
}
