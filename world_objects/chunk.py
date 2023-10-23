import random

from settings import *
from meshes.chunk_mesh import ChunkMesh


class Chunk:
    def __init__(self, world, position):
        self.app = world.app
        self.world = world
        self.position = position
        self.m_model = self.get_model_matrix()
        self.voxels: np.array = None
        self.mesh: ChunkMesh = None
        self.is_empty = True

        self.center = (glm.vec3(self.position) + 0.5) * CHUNK_SIZE
        self.is_on_frustum = self.app.player.frustum.if_on_frustum

    def get_model_matrix(self):
        x, y, z = self.position
        return glm.translate(glm.mat4(), glm.vec3(x, y, z) * CHUNK_SIZE)

    def set_uniform(self):
        self.mesh.program["m_model"].write(self.m_model)

    def build_mesh(self):
        self.mesh = ChunkMesh(self)

    def render(self):
        if self.is_empty and self.is_on_frustum(self):
            return
        self.set_uniform()
        self.mesh.render()

    def generate_simplex_noise(self, *vector):
        return int(glm.simplex(glm.vec2(*vector) * 0.005) * 32 + 32)

    def generate_sin(self, *sin_range, x):
        return int(
            sin_range[0]
            + sin_range[1] * np.sin(np.pi * x / (sin_range[1] * sin_range[1]))
        )

    def build_voxels(self):
        # empty chunk
        voxels = np.zeros(CHUNK_VOL, dtype="uint8")

        # fill chunk
        cx, cy, cz = glm.ivec3(self.position) * CHUNK_SIZE

        rng = random.randrange(1, 100)

        for x in range(CHUNK_SIZE):
            wx = x + cx
            for z in range(CHUNK_SIZE):
                wz = z + cz

                # world height calculated with simplex noise
                # For this specific voxel column, it will return
                # the height for that point in the chunk, e.g. how many
                # voxels in that column
                world_height = self.generate_simplex_noise(wx, wz)
                # print("world height at wx", wx, world_height)
                local_height = min(world_height - cy, CHUNK_SIZE)
                for y in range(local_height):
                    wy = y + cy

                    # the `voxel_id` is the "type" of voxel
                    # e.g. grass, dirt, stone, etc.
                    voxel_id = rng
                    voxels[x + CHUNK_SIZE * z + CHUNK_AREA * y] = voxel_id

        if np.any(voxels):
            self.is_empty = False

        return voxels
