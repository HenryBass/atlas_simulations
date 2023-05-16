from math import *
import numpy as np
import matplotlib.pyplot as plt
from opensky_api import OpenSkyApi
import random
from scipy.spatial import ConvexHull, convex_hull_plot_2d

api = OpenSkyApi()

def llarToWorld(lat, lon, alt, rad):
    x = rad * cos(lat) * cos(lon) + alt * cos(lat) * cos(lon)
    y = rad * cos(lat) * sin(lon) + alt * cos(lat) * sin(lon)
    z = rad * sin(lat) + alt * sin(lat)

    return np.array([x, y, z])

fig = plt.figure()
ax = plt.axes(projection='3d')

def write():
    states = api.get_states()
    f = open("data.txt", "w")

    for s in states.states:
        print("(%r, %r, %r, %r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity))

        if s.longitude != None and s.latitude != None and s.baro_altitude != None and s.on_ground == False:
            f.writelines("%r, %r, %r\n" % (s.longitude, s.latitude, s.baro_altitude))

    f.close()

def read():
    f = open("data.txt", "r")
    lines = f.readlines()
    f.close()

    xs = np.array([])
    ys = np.array([])
    zs = np.array([])

    for line in lines:
        line = line.split(", ")
        lon = float(line[0])
        lat = float(line[1])
        alt = float(line[2])

        c = llarToWorld((lat * 0.0174532925), (lon * 0.0174532925), alt, 6378100)
        #c = np.array([(360 * random.random()) - 180,
        #              (360 * random.random()) - 180,
        #              random.random() * 10])
        xs = np.append(xs, c[0])
        ys = np.append(ys, c[1])
        zs = np.append(zs, c[2])

    ax.scatter3D(xs, ys, zs, c='r', marker='.')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    cs = np.dstack((xs, ys, zs))[0]

    hull = ConvexHull(cs)
    print((hull.vertices.shape[0] / 6145) * 100)
    #print(ConvexHull(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
    #ax.scatter3D(cs, c='b', marker='o')
    plt.show()

#write()
read()
