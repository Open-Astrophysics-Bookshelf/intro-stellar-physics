import numpy as np
from scipy.stats import cauchy, norm
import matplotlib.pyplot as plt

sig = 1.0/(2.0*np.sqrt(2.0*np.log(2.0)))
hml = cauchy.pdf(0.5,scale=0.5)
hmg = norm.pdf(0.5,scale=sig)

plt.style.use('text-sans')
plt.rc('xtick',**{'direction':'out'})
plt.rc('ytick',**{'direction':'out'})
plt.rc('font',**{'size':9})
plt.figure(figsize=(2,2))
x = np.linspace(-3.3,3.3,128)
plt.xlim(-1.7,1.7)
plt.ylim(-0.1,1.1)
plt.plot(x,cauchy.pdf(x,scale=0.5),'k-',label=r'$\mathcal{L}$')
plt.plot(x,norm.pdf(x,scale=sig),'k:',label=r'$\mathcal{G}$')
plt.vlines([-0.5,0.5],-0.1,1.1,linewidth=0.5,color='0.5')
plt.plot([-0.5,-0.5,0.5,0.5],[hmg,hml,hmg,hml],marker='_',linestyle='none',markersize=4,markerfacecolor='0.2',markeredgecolor='0.2')
plt.xlabel(r'$\nu-\nu_0$')
plt.xticks([-1.5,-0.5,0.5,1.5])
plt.yticks([0.0,0.5,1.0])
plt.legend()
plt.savefig('comparison.pdf',format='pdf',bbox_inches='tight')
