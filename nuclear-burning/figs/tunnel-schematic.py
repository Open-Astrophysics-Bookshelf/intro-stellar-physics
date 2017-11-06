import numpy as np
import matplotlib.pyplot as plt

plt.style.use('text-sans')
ax = plt.figure(figsize=(5,5*0.618)).add_subplot(111)
ax.set_xlim(0.0,5.0)
ax.set_ylim(-5.0,7.0)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.set_xlabel(r'$r$')
ax.set_ylabel(r'$E$')

# Coulomb
rc = np.linspace(0.3,5.0)
Ec = 3.0/rc
plt.plot(rc,Ec,color='r')
# nuclear
plt.plot([0.05,0.05],[-5.0,7.0],color='b')
plt.plot([0.5,0.5],[-5.0,6.0],color='b')

# energy
plt.plot([0.05,0.5],[1.0,1.0],color='k',linestyle='-')
plt.plot([0.5,3.0],[1.0,1.0],color='k',linestyle=':')
plt.plot([3.0,5.0],[1.0,1.0],color='k',linestyle='-')

# wavefunction
r_out = np.linspace(3.0,5.0,41)
psi_out = 5.0*np.sin(2.0*np.pi*(r_out - 3.0) + 0.25*np.pi)
plt.plot(r_out,psi_out,color='0.7',linewidth=1.0)

r_tunnel = np.linspace(0.5,3.0,26)
psi_tunnel = 5.0*np.exp((r_tunnel-3.0))*np.sin(0.25*np.pi)
plt.plot(r_tunnel,psi_tunnel,color='0.7',linewidth=1.0)

r_in = np.linspace(0.05,0.5,26)
psi_in = np.cos(2.0*np.pi*(0.5-r_in) + 0.082)
plt.plot(r_in,psi_in,color='0.7',linewidth=1.0)

plt.show()
