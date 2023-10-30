from settings import *
from meshes.hud_mesh import HudMesh


class Hud:
    def __init__(self, world):
        self.app = world.app
        self.world = world
        self.position = glm.vec3(0)
        self.mesh = HudMesh(self.app)

    def update(self):
        pass

    def render(self):
        self.mesh.render()
