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

    def get_model_matrix(self):
        x, y, z = self.position
        return glm.translate(glm.mat4(), glm.vec3(x, y, z) * CHUNK_SIZE)

    def set_uniform(self):
        self.mesh.program["m_model"].write(self.m_model)

    def build_mesh(self):
        self.mesh = ChunkMesh(self)

    def render(self):
        self.set_uniform()
        self.mesh.render()

    def build_voxels(self):
        # empty chunk
        voxels = np.zeros(CHUNK_VOL, dtype="uint8")

        # fill chunk
        cx, cy, cz = glm.ivec3(self.position) * CHUNK_SIZE

        for x in range(CHUNK_SIZE):
            for z in range(CHUNK_SIZE):
                wx = x + cx
                wz = z + cz

                # world height calculated with simplex noise
                world_height = int(
                    glm.simplex(  # simplex noise
                        glm.vec2(wx, wz) * 0.0053  # scale
                    ) * 10 + 20  # height
                )
                local_height = min(world_height - cy, CHUNK_SIZE)
                for y in range(local_height):
                    wy = y + cy
                    voxels[x + CHUNK_SIZE * z + CHUNK_AREA * y] = wy + 1
        return voxels
