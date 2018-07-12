import numpy as np
import matplotlib.pyplot as plt

def TP(P,T0,P0,gamma = 2/5):
    return T0*(P/P0)**gamma

def make_plot(ax,p,gamma):
    t = TP(p,1.0,1.0,gamma=gamma)
    lgt = np.log10(t)
    lgp = np.log10(p)
    pad = max(0.1*(lgt.max()-lgt.min()),0.5)
    ax.set_xlim(lgp.min(),lgp.max())        
    ax.set_ylim(lgt.min()-pad,lgt.max()+pad)
    ax.grid(color='0.5',linestyle=':',linewidth=0.5)
    ax.plot(np.log10(p),np.log10(t),color='k')

def super_adiabat_plot(ax,p):
    make_plot(ax,p,3/5)

def isothermal_plot(ax,p):
    make_plot(ax,p,0)

def sub_adiabat_plot(ax,p):
    make_plot(ax,p,1/5)
    
def rising_plot(ax,p):
    make_plot(ax,p,-1/5)

def Trho_plot(ax,lgrho,lgT):
    ax.set_xlim(-3,7)
    ax.set_ylim(5,7.7)
    ax.grid(color='0.5',linestyle=':',linewidth=0.5)
    ax.set_xlabel(r'$\log(\rho\,/\,\mathrm{kg\,m^{-3}})$')
    ax.set_ylabel(r'$\log(T\,/\,\mathrm{K})$')
    ax.plot(lgrho,lgT,'k^',markersize=4)

plt.style.use('text-sans')
#plt.rc('font',**{'size':9})
plt.rc('axes',**{'axisbelow':True,'titlesize':'medium'})

# First exercise: which one is unstable to convection?
fig = plt.figure(figsize=(6,4))
seq = [1,2,3,4]
methods = [super_adiabat_plot,isothermal_plot,sub_adiabat_plot,rising_plot]
np.random.shuffle(seq)
for i,method in zip(seq,methods):
    ax = fig.add_subplot(2,2,i)
    ax.set_ylabel(r'$\log(T\,/\,T_0)$')
    ax.set_xlabel(r'$\log(P\,/\,P_0)$')
    p = np.logspace(-5.0,0.0,50)
    method(ax,p)

plt.tight_layout()
plt.savefig('convection-worksheet-1.pdf',format='pdf',bbox_inches='tight')


# Next exercise: sketch layout of star in T-rho plane. Do this for 3 stars: 
# fully adiabatic; radiative core, adiabatic outer; adiabatic core, radiative 
# outer

fig = plt.figure(figsize = (6,2))
lgrhos = [5,4.5,3.2]
lgTs = [6.75,7.2,7.6]
plots = ['fully convective','radiative core','radiative envelope']
for i in range(3):
    ax = fig.add_subplot(1,3,i+1)
    ax.set_title(plots[i])
    Trho_plot(ax,lgrhos[i],lgTs[i])
    if i > 0:
        ax.vlines(1.0,5,7.7,linewidth=0.5,color='r',linestyle='-')
plt.tight_layout()
plt.savefig('convection-worksheet-2.pdf',format='pdf',bbox_inches='tight')

