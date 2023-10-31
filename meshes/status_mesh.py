from settings import *
from meshes.base_mesh import BaseMesh


class StatusMesh(BaseMesh):
    def __init__(self, world):
        super().__init__()
        self.world = world
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
                -WINDOW_ASPECT_RATIO,  -1.0,  # bottom left
                -0.75, -1.0,  # bottom right
                -0.75, -0.8,  # top right

                -0.75, -0.8,  # top right
                -WINDOW_ASPECT_RATIO,  -0.8,  # top left
                -WINDOW_ASPECT_RATIO,  -1.0,  # bottom left
            ],
            dtype="f4",
        )
        # fmt: on

        return vertex_data
