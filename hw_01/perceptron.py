import numpy as np

xy = np.array( [
    [-1,  -1,  1], 
    [ 1,   0, -1],
    [-1, 1.5,  1],
])


T = 10 #number of runs
N = len(xy) #number of samples

theta = np.array([0,0], dtype=np.float64)
theta_0 = 0

m = 0 #number of mistakes until it converges
i_0 = 1 #algorithm starts with i_0'th sample

if __name__ == '__main__':

    for j in range(T):
        for i in range(N):
            ith = (i + i_0) % N
            # print('ith = ' + str(ith))
            x = xy[ith][0:2]
            y = xy[ith][2]
            # print('x = ', str(x))
            # print('y = ', str(y))
            # print('theta = ' + str(theta))

            z = y * (np.dot(x, theta))
            print('z = ' + str(z))
            if z <=0:
                m +=1
                print('MISTAKE ['+str(m)+']')
                theta += y*x
                print('theta = ' + str(theta))
            else:
                print('SUCCESS: theta = ['+str(theta)+']')


        input()
