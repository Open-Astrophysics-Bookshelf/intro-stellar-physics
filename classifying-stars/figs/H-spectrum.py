import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt

def wavelength(n,m):
    lam0 = (1+sc.m_e/sc.m_p)/sc.Rydberg * 1.0e9 # nm
    if n > m: n,m = m,n
    return lam0/(1/n**2 - 1/m**2)

width = 2
height = 2*1.6

plt.style.use('text-sans')
plt.rc('xtick',**{'direction':'out'})
plt.rc('font',**{'size':8})

Nlines = 20
greek = [r'$\alpha$',r'$\beta$',r'$\gamma$',r'$\delta$',r'$\epsilon$']

Lyman = [ wavelength(1,m) for m in range(2,2+Nlines) ]
Balmer = [ wavelength(2,m) for m in range(3,3+Nlines) ]
Paschen = [ wavelength(3,m) for m in range(4,4+Nlines) ]

plt.figure(figsize=(width,height))
plt.gca().get_xaxis().set_visible(False)
xmin,xmax = plt.xlim(0,1)
plt.ylim(20,1500)

plt.hlines(Lyman,xmin,xmax,color='0.5',linestyle='-',linewidth=0.5)
plt.annotate(s=r'Lyman ($m\to 1$)',fontsize='small',xytext=(3,-1),
    textcoords='offset points',xy=(0,Lyman[-1]),
    va='top',ha='left')

plt.hlines(Balmer,xmin,xmax,color='0.5',linestyle='-',linewidth=0.5)
plt.annotate(s=r'Balmer ($m\to 2$)',fontsize='small',xytext=(3,-1),
    textcoords='offset points',xy=(0,Balmer[-1]),
    va='top',ha='left')
plt.annotate(s=r'$3\to2$',fontsize='small',xy=(0.5,Balmer[0]),
    va='bottom',ha='center')
plt.annotate(s=r'$4\to2$',fontsize='small',xy=(0.5,Balmer[1]),
    va='bottom',ha='center')

plt.hlines(Paschen,xmin,xmax,color='0.5',linestyle='-',linewidth=0.5)
plt.annotate(s=r'Paschen ($m\to 3$)',fontsize='small',xytext=(3,-1),
    textcoords='offset points',xy=(0,Paschen[-1]),
    va='top',ha='left')
plt.annotate(s=r'$5\to3$',fontsize='small',xy=(0.5,Paschen[1]),
    va='bottom',ha='center')
plt.annotate(s=r'$6\to3$',fontsize='small',xy=(0.5,Paschen[2]),
    va='bottom',ha='center')

plt.ylabel(r'$\lambda$ (nm)')
plt.savefig('H-spectrum.pdf',format='pdf',bbox_inches='tight')
