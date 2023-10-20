from numba import njit
import os
import numpy as np
import glm
import math


os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "DISABLE"

FPS = 0

# resolution of the screen
WIN_RES = glm.vec2(1800, 1200)

# chunk
CHUNK_SIZE = 64
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE
CHUNK_VOL = CHUNK_AREA * CHUNK_SIZE

# world
WORLD_W, WORLD_H = 4, 1
WORLD_D = WORLD_W
WORLD_AREA = WORLD_W * WORLD_D
WORLD_VOL = WORLD_AREA * WORLD_H

# world center
CENTER_XZ = WORLD_W * H_CHUNK_SIZE
CENTER_Y = WORLD_H * H_CHUNK_SIZE


# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)  # vertical fov
H_FOV = 2 * glm.atan(glm.tan(V_FOV / 2) * ASPECT_RATIO)  # horizontal fov
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89.0)

# player
PLAYER_SPEED = 0.050
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(CENTER_XZ, WORLD_H * CHUNK_SIZE, CENTER_XZ)
MOUSE_SENSITIVITY = 0.002

# colours
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)
