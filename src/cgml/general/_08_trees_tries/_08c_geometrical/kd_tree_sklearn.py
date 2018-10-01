# Applications:
#

from sklearn.neighbors import KDTree

#Query for k-nearest neighbors
import numpy as np
import pickle
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import matplotlib.patches as patches
np.random.seed(0)
X = np.random.random((10, 2))  # 10 points in 2 dimensions

tree = KDTree(X, leaf_size=1)

dist, ind = tree.query(X[:1], k=4)
print(X[:1], ind)   # indices of 3 closest neighbors
print(dist)         # distances to 3 closest neighbors


# Pickle and Unpickle a tree. Note that the state of the tree is saved in the pickle operation: the tree needs not be rebuilt upon unpickling.
X = np.random.random((10, 2))  # 10 points in 3 dimensions
tree = KDTree(X, leaf_size=2)        
s = pickle.dumps(tree)                     
tree_copy = pickle.loads(s)                
dist, ind = tree_copy.query(X[:1], k=3)     
print(ind)  # indices of 3 closest neighbors
print(dist)  # distances to 3 closest neighbors


# Query for neighbors within a given radius
np.random.seed(0)
X = np.random.random((100, 2))
tree = KDTree(X, leaf_size=1)
# print(tree.query_radius(X[:1], r=0.3, count_only=True))
ind = tree.query_radius(X[:1], r=0.3)

def plot_kd_tree_radius(X, ind, r):
    fig, ax = plt.subplots()

    ax.add_collection(PatchCollection([patches.Circle((X[0, 0], X[0, 1]), radius=r, edgecolor='black',facecolor=None)]))
    ax.scatter(X[:, 0], X[:, 1])
    for idx in ind: ax.scatter(X[idx, 0], X[idx, 1])
    ax.scatter(X[0, 0], X[0, 1])
    plt.show()

plot_kd_tree_radius(X, ind, r=0.3)



# Compute a gaussian kernel density estimate:
np.random.seed(1)
X = np.random.random((100, 2))
tree = KDTree(X)                
kdensity = tree.kernel_density(X[:3], h=0.1, kernel='gaussian')



# Compute a two-point auto-correlation function
np.random.seed(0)
X = np.random.random((30, 2))
r = np.linspace(0, 1, 5)
tree = KDTree(X)                
kcorr = tree.two_point_correlation(X, r)
