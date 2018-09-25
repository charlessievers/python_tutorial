# Open up an xyz file of caffeine and find the smallest distance between any two atoms
import numpy as np


def read_xyz(filename):

    atoms = []
    coordinates = []
    xyz = open(filename)
    n_atoms = int(xyz.readline())
    title = xyz.readline()

    for line in xyz:
        atom, x, y, z = line.split()
        atoms.append(atom)
        coordinates.append([float(x), float(y), float(z)])
    xyz.close()

    if n_atoms != len(coordinates):
        raise ValueError("File says {} atoms but read {} points.".format(n_atoms, len(coordinates)))

    return np.array(coordinates)

coords = read_xyz('caffeine.xyz')
print(coords)