import numpy as np
import matplotlib.pyplot as plt

# input as an array of [xi_0, xi_1, y_i]
xy = np.array( [
    [-1,  -1,  1], 
    [ 1,   0, -1],
    [-1,  10,  1],
])

T = 10 #number of runs
N = len(xy) #number of samples

theta = np.array([0,0], dtype=np.float64)
theta_0 = 0
thetas = []

m = 0 #number of mistakes until it converges
i_0 = 1 #algorithm starts with i_0'th sample
print('Starting with x({})...'.format(i_0 +1))


if __name__ == '__main__':
    for j in range(T):
        failed = False
        for i in range(N):
            ith = (i + i_0) % N
            # print('ith = ' + str(ith))
            x = xy[ith][0:2]
            y = xy[ith][2]
            # print('x = ', str(x))
            # print('y = ', str(y))
            # print('theta = ' + str(theta))

            z = y * (np.dot(x, theta))
            # print('z = ' + str(z))
            if z <=0:
                failed = True
                m +=1
                # print('MISTAKE ['+str(m)+']')
                theta += y*x
                # print('  theta = ' + str(theta))
                thetas.append(theta.tolist())
            else:
                #print('SUCCESS: theta = ['+str(theta)+']')
                pass

        if failed:
            print('Failed. Run another (#{}) iteration?'.format(j+2))
            pass
        else:
            print('The algorithm has converged to the following:')
            print('  theta = ['+str(theta)+']')
            print('  after {} mistakes'.format(m))
            print('  Progression of theta: {}'.format(thetas))
            break

    # Plot the samples (positive 'blue' and negative 'red')
    x1s = [(xy[i][0]) for i in range(len(xy))]
    x2s = [(xy[i][1]) for i in range(len(xy))]
    ys  = ['red' if (xy[i][2]) == -1 else 'blue' for i in range(len(xy))]
    print(ys)
    plt.scatter(x1s, x2s, s=100, c=ys)

    x = np.linspace(-10, 10, 100)
    decision_b = 2 * x + 3
    plt.plot(x, decision_b)
    plt.show()