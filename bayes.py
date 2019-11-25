import numpy as np 

print("Version {}".format(np.__version__))

x = np.array([[0,1,0,1],
            [1,0,1,1],
            [0,0,0,1],
            [1,0,1,0]]
)

y = np.array([0,1,0,1])

counts = {}
for label in np.unique(y):
    counts[label] = x[y==label].sum(axis=0)

print("Feature counts . \n{}".format(counts))
