import numpy as np

xy = np.array( [
    [[-1,  -1],  1], 
    [[ 1,   0], -1],
    [[-1, 1.5],  1],
])


t = 10
n = 3
while True:
    for i in range(n):
        print(xy[i][0])
        print(xy[i][1])


    input()
