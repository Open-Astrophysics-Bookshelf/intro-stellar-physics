import matplotlib.pyplot as plt
import numpy as np

def hop(r0,l=1.0):
    ang = 2.0*np.pi*np.random.random()
    return r0 + l*np.array([np.cos(ang),np.sin(ang)])

plt.style.use('text-sans')
plt.figure(figsize=(2,2))
NARROWS=20


if __name__ == "__main__":
    r = np.zeros(2)
    NHOPS = 1000
    print('{0:5.2f}    {1:5.2f}'.format(r[0],r[1]))
    x = np.zeros(NHOPS)
    y = np.zeros(NHOPS)
    for i in range(NHOPS):
        r = hop(r)
        x[i] = r[0]
        y[i] = r[1]
        if i % 20 == 0:
            print('{0:5.2f}    {1:5.2f}'.format(r[0],r[1]))
    print('\n\n')
    print('{0:5.2f}    {1:5.2f}'.format(x.mean(),y.mean()))
    print('{0:5.2f}    {1:5.2f}'.format(x.std(),y.std()))