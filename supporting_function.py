import numpy as np

#create LxL matrix
def make_lattice (L, mode = "random"):
    if mode == "random":
        lattice = np.random.choice([-1,1], size=(L,L))
    elif mode == "up":
        lattice = np.ones((L, L), dtype=int)
    elif mode == "down":
        lattice = -np.ones((L, L), dtype=int)
    return lattice

# calculate the total energy (E) and energy per spin (e) of the given lattice
def calc_E_e(lattice, J=1.0, h=0.0):
    down = np.roll(lattice, -1, axis=0)
    right = np.roll(lattice, -1, axis=1)
    pair_sum = np.sum(lattice * down) + np.sum(lattice * right)
    E = -J * pair_sum - h * np.sum(lattice)
    e = E/lattice.size
    return E, e


"""



"""

# calculate the total magnetism (M) and magnetization per spin (m)
def calc_M_m(lattice):
    M = np.sum(lattice)
    m = M/lattice.size
    return M, m

# applying periodic boundary conditions to calculate the energy change due to flipping
def calc_flip_E (lattice, i, j, J=1.0, h=0.0):
    L = lattice.shape[0]
    up = lattice[(i-1)% L,j] 
    left = lattice[i, (j-1)% L]
    down = lattice[(i+1)% L,j]
    right = lattice[i, (j+1)% L]

    nn_sum = (up + left + down + right)
    # note : 2 * h * lattice[i,j] is optional 
    E_flip = 2 * J * lattice[i,j] * nn_sum + 2 * h * lattice[i,j]
    return E_flip

