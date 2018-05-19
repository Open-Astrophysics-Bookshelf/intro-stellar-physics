import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt

plt.style.use('text-sans')
plt.rc('font',**{'size':9})

def planck(lam_nm,T):
    lam = lam_nm*1.0e-9
    x = sc.h*sc.c/sc.k/lam/T
    return 2.0e-9*sc.h*sc.c**2/lam**5/(np.exp(x)-1)

lam = np.logspace(1.7,4.3,256)
width= 2.0
aspect = 1.0
plt.figure(figsize=(width,aspect*width))
plt.xlim(100.0,10000.0)
mB = planck(lam,8000).max()
plt.ylim(1.0e-3*mB,mB)
plt.xlabel(r'$\lambda$ [nm]')
plt.ylabel(r'$B_\lambda$ [$\mathrm{W\,m^{-2}\,nm^{-1}}$]')
for temp in np.arange(3000,7500,500):
    b = planck(lam,temp)
    plt.loglog(lam,b,color='black',linewidth=0.5)
    lam_pk = 290*10000/temp
    if temp % 1000 == 0:
        plt.annotate(s='{} K'.format(temp),
            xy=(lam_pk,b.max()),ha='right',size='small')
plt.savefig('Planck.pdf',format='pdf',bbox_inches='tight')
