from settings import *
from meshes.base_mesh import BaseMesh


class HudMesh(BaseMesh):
    def __init__(self, world):
        super().__init__()
        self.app = world.app
        self.ctx = self.app.ctx
        self.program = self.app.shader_program.hud

        self.vbo_format = "2f"
        self.attrs = ("in_vert",)
        self.vao = self.get_vao()

    def get_vertex_data(self):
        # fmt: off
        vertex_data = np.array(
            [
                # x, y
                -0.005, 0.005,  # bottom left
                 0.005, 0.005,  # bottom right
                 0.005, 0.055,  # top right

                 0.005, 0.055,  # top right
                -0.005, 0.055,  # top left
                -0.005, 0.005,  # bottom left


                -0.005, -0.055,  # bottom left
                 0.005, -0.055,  # bottom right
                 0.005, -0.005,  # top right

                 0.005, -0.005,  # top right
                -0.005, -0.005,  # top left
                -0.005, -0.055,  # bottom left


                0.005, -0.005,  # bottom left
                0.055, -0.005,  # bottom right
                0.055,  0.005,  # top right

                0.055,  0.005,  # top right
                0.005,  0.005,  # top left
                0.005, -0.005,  # bottom left


                -0.055, -0.005,  # bottom left
                -0.005, -0.005,  # bottom right
                -0.005,  0.005,  # top right

                -0.005,  0.005,  # top right
                -0.055,  0.005,  # top left
                -0.055, -0.005,  # bottom left
            ],
            dtype="f4",
        )
        # fmt: on

        return vertex_data
