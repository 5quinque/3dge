from settings import *


class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.player = app.player
        # --- Shader Programs ---
        self.chunk = self.get_program(shader_name="chunk")
        self.voxel_marker = self.get_program(shader_name="voxel_marker")
        self.hud = self.get_program(shader_name="hud")
        # ------------------------
        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        # chunk
        self.chunk["m_proj"].write(self.player.m_proj)
        self.chunk["m_model"].write(glm.mat4())
        self.chunk["u_texture_0"] = 0

        # voxel_marker
        self.voxel_marker["m_proj"].write(self.player.m_proj)
        self.voxel_marker["m_model"].write(glm.mat4())
        self.voxel_marker["u_texture_0"] = 0

        # hud
        self.hud["projection"].write(
            glm.ortho(-WINDOW_ASPECT_RATIO, WINDOW_ASPECT_RATIO, -1, 1, -1, 1)
        )

    def update(self):
        self.chunk["m_view"].write(self.player.m_view)
        self.voxel_marker["m_view"].write(self.player.m_view)

    def get_program(self, shader_name):
        with open(f"shaders/{shader_name}.vert", "r") as f:
            vertex_shader_source = f.read()

        with open(f"shaders/{shader_name}.frag", "r") as f:
            fragment_shader_source = f.read()

        program = self.ctx.program(
            vertex_shader=vertex_shader_source, fragment_shader=fragment_shader_source
        )

        return program
