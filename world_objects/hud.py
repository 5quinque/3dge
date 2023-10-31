from settings import *
from meshes.hud_mesh import HudMesh
from meshes.status_mesh import StatusMesh


class Hud:
    def __init__(self, world):
        self.app = world.app
        self.world = world
        self.position = glm.vec3(0)
        self.hud_mesh = HudMesh(self.world)
        self.status_mesh = StatusMesh(self.world)

    def set_uniform(self):
        self.status_mesh.program["mode_id"] = self.world.voxel_handler.interaction_mode

    def update(self):
        pass

    def render(self):
        self.set_uniform()

        self.hud_mesh.render()
        self.status_mesh.render()
