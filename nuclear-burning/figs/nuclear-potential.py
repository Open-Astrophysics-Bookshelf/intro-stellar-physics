import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

Vm = 25.0
Rm = 0.7
E = -2.2

def potential(r):
    return Vm*(2*(Rm/r)**6 - 3*(Rm/r)**4)

def turning_point(r):
    return potential(r) - E

r = np.linspace(0.1,2.5,100)
v = potential(r)
tp1 = brentq(turning_point,0.1,0.6)
tp2 = brentq(turning_point,0.6,2.0)
print('turning points = ',tp1,tp2)
plt.style.use('text-sans')
textwidth=2
ax = plt.figure(figsize=(textwidth,textwidth*0.618)).add_subplot(111)
ax.set_xlim(0.0,2.5)
ax.set_ylim(1.1*v.min(),6.0)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks([1.0,2.0])
ax.yaxis.set_ticks([])
ax.set_xlabel(r'$r$ (fm)',x=0.8)
ax.set_ylabel(r'$V$, $E$ (MeV)')

# nuclear
plt.plot(r,v,color='b',linewidth=1)

# energy
plt.plot([tp1,tp2],[E,E],color='k',linestyle=':')

plt.savefig('nuclear-potential.pdf',format='pdf')
