import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

def plot_one(n,ax):
    theta = np.linspace(0.0,2.0*np.pi,100)
    mu = np.cos(theta-np.pi/2)
    p = legendre(n)
    r = p(mu)
    x, y = r*np.cos(theta), r*np.sin(theta)
    ax.set_aspect('equal')
    ax.plot(x,y,color='k',linewidth=1,zorder=3)
    ax.set_title(r'$n={0}$'.format(n),size=8)
    ax.spines['left'].set_position(('zero'))
    ax.spines['left'].set_color('0.5')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('zero'))
    ax.spines['bottom'].set_color('0.5')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xlim(-1.1,1.1)
    ax.set_ylim(-1.1,1.1)
    ax.set_xticks([-1.0,-0.5,0.5,1.0])
    ax.set_yticks([-1.0,-0.5,0.5,1.0])
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    ax.xaxis.set_tick_params(direction='inout')
    ax.yaxis.set_tick_params(direction='inout')
    
plt.figure(figsize=(6.6,3.3))
plt.style.use('text-sans')
plt.rc('xtick',**{'color':'0.5'})
plt.rc('ytick',**{'color':'0.5'})

for n in range(8):
    ax = plt.subplot(2,4,n+1)
    plot_one(n,ax)

plt.savefig('legendre.pdf',format='pdf',bbox_inches='tight')
