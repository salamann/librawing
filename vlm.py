import numpy as np


def vortex_lattice(aspect_ratio, nx, ny, alpha):
    dx = 1.0 / float(nx)
    dy = aspect_ratio / (2.0 * ny + 0.5)
    neqns = nx * ny
    cos_alpha = np.cos(np.radians(alpha))
    sin_alpha = np.sin(np.radians(alpha))
    