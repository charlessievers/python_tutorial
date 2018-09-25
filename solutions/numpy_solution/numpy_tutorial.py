import numpy as np
import time


def read_xyz(filename):

    """Read filename in XYZ format and return lists of atoms and coordinates.

    If number of coordinates do not agree with the statd number in
    the file it will raise a ValueError.
    """

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


def fsd(coords):
    start = time.time()
    sd = 0
    for coord1 in coords:
        for coord2 in coords:
            if (coord1 != coord2).all():
                if np.linalg.norm(coord2-coord1) < sd or sd == 0:
                    sd = np.linalg.norm(coord2-coord1)
    end = time.time()
    print(end - start)
    return sd**0.5


def fast_fsd(coords):
    start = time.time()
    coord1 = coords[:, np.newaxis]
    coord2 = coords[np.newaxis, :]
    diff = coord2 - coord1
    dist = np.linalg.norm(diff, axis=-1)**0.5
    end = time.time()
    print(end - start)
    return np.min(dist[np.nonzero(dist)])


if __name__ == "__main__":

    caffeine = read_xyz('/Users/charliesievers/PycharmProjects/Object_Oriented_Tutorial/tutorial/numpy_tutorial/caffeine.xyz')
    print(fsd(caffeine))
    print(fast_fsd(caffeine))
