from settings import *
from meshes.base_mesh import BaseMesh


class HudMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.ctx = self.app.ctx
        self.program = self.app.shader_program.hud

        self.vbo_format = "2f 4f"
        self.attrs = ("in_vert", "in_color")
        self.vao = self.get_vao()

    def get_vertex_data(self):
        # fmt: off
        vertex_data = np.array(
            [
                # x, y, r, g, b, a
                -0.005, 0.005, 0.0, 0.4, 0.7, 0.75,  # bottom left
                 0.005, 0.005, 0.0, 0.4, 0.7, 0.75,  # bottom right
                 0.005, 0.055, 0.0, 0.4, 0.7, 0.75,  # top right

                 0.005, 0.055, 0.0, 0.4, 0.7, 0.75,  # top right
                -0.005, 0.055, 0.0, 0.4, 0.7, 0.75,  # top left
                -0.005, 0.005, 0.0, 0.4, 0.7, 0.75,  # bottom left


                -0.005, -0.055, 0.0, 0.4, 0.7, 0.75,  # bottom left
                 0.005, -0.055, 0.0, 0.4, 0.7, 0.75,  # bottom right
                 0.005, -0.005, 0.0, 0.4, 0.7, 0.75,  # top right

                 0.005, -0.005, 0.0, 0.4, 0.7, 0.75,  # top right
                -0.005, -0.005, 0.0, 0.4, 0.7, 0.75,  # top left
                -0.005, -0.055, 0.0, 0.4, 0.7, 0.75,  # bottom left


                0.005, -0.005, 0.0, 0.4, 0.7, 0.75,  # bottom left
                0.055, -0.005, 0.0, 0.4, 0.7, 0.75,  # bottom right
                0.055,  0.005, 0.0, 0.4, 0.7, 0.75,  # top right

                0.055,  0.005, 0.0, 0.4, 0.7, 0.75,  # top right
                0.005,  0.005, 0.0, 0.4, 0.7, 0.75,  # top left
                0.005, -0.005, 0.0, 0.4, 0.7, 0.75,  # bottom left


                -0.055, -0.005, 0.0, 0.4, 0.7, 0.75,  # bottom left
                -0.005, -0.005, 0.0, 0.4, 0.7, 0.75,  # bottom right
                -0.005,  0.005, 0.0, 0.4, 0.7, 0.75,  # top right

                -0.005,  0.005, 0.0, 0.4, 0.7, 0.75,  # top right
                -0.055,  0.005, 0.0, 0.4, 0.7, 0.75,  # top left
                -0.055, -0.005, 0.0, 0.4, 0.7, 0.75,  # bottom left
            ],
            dtype="f4",
        )
        # fmt: on

        return vertex_data
