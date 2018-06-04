
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

#name, type, suptype, num. index, L/Lsun, Teff, r, g, b
star_data = np.genfromtxt(
    'stellar_parameters.data',names=[
        'star','type','subtype','indx','L','Teff','red','green','blue'],
        dtype=None)

clrs = [(r*0.01,g*0.01,b*0.01) \
    for r,g,b in zip(star_data['red'],star_data['green'],star_data['blue'])]

plt.style.use('text-sans')
# rc('font',**{'size':14})
width = 2.0
rc('figure',**{'figsize':(width,width/0.618),'facecolor':'none'})
rc('axes',**{'facecolor':(0.2,0.0,0.2)})
# rc('ytick',**{'direction':'out'})
# rc('xtick',**{'direction':'out'})
xs = star_data['indx']+star_data['subtype']*0.1
plt.xticks(np.arange(0.5,7),'OBAFGKM')
plt.xlim(0,7.4)
plt.ylim(10**(-2.2),10**(6.5))
for stype,sub,x,l,clr in \
    zip(star_data['type'],star_data['subtype'],xs,star_data['L'],clrs):
    plt.semilogy(
        x,l,linestyle='none',marker='o',markersize=8,mfc=clr,mec='none')
    plt.annotate(s=str(stype,'utf-8')+str(sub),xy=(x,l),
        ha='left',va='bottom',size='x-small',
        xytext=(4,4),textcoords='offset points',color=clr)
plt.ylabel('luminosity relative to solar')
plt.tick_params(axis='y',which='major',right='off')
plt.tick_params(axis='x',which='major',top='off')
plt.minorticks_off()
plt.savefig('HR.pdf',format='pdf',bbox_inches='tight',facecolor='none', edgecolor='none',transparent=False)
