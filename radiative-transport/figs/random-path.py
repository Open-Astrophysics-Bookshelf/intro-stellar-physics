import matplotlib.pyplot as plt
import numpy as np

def hop(n,l=1.0):
    ang = 2.0*np.pi*np.random.random(n)
    return np.array([l*np.cos(a) for a in ang]), np.array([l*np.sin(a) for a in ang])

plt.style.use('text-sans')
N_ARROWS=50
hop_x,hop_y = hop(N_ARROWS)
cum_x = hop_x.cumsum()
cum_y = hop_y.cumsum()

extent = max(np.abs(cum_x).max(),np.abs(cum_y).max())
x = 0.0
y = 0.0
plt.figure(figsize=(2,2))
plt.xlim(-extent,extent)
plt.ylim(-extent,extent)
dalpha = 1/N_ARROWS
alpha = dalpha
for dx,dy in zip(hop_x,hop_y):
    plt.arrow(x,y,dx,dy,
        length_includes_head=True,
        width=0.001,
        color='black',
        alpha = alpha)
    x += dx
    y += dy
    alpha += dalpha
plt.axis('off')
plt.savefig('random-walk-schematic.pdf',format='pdf',bbox_inches='tight')

