import numpy as np
import matplotlib.pyplot as plt

def get_spectra(fname):
    inarr = np.genfromtxt(fname,skip_footer=1)
    footarr = np.genfromtxt(fname,skip_header=399)
    l = inarr[:,0]
    f = np.append(inarr[:,1:].flatten(),footarr[1:])
    lam = np.zeros_like(f)
    lext = np.array([1.4*j for j in range(7)])
    for i in range(399):
        lam[7*i:7*i+7] = l[i]+lext[:]
    lam[7*399:] = footarr[0]+lext[0:-1]
    f = f/f.max()
    lam *= 0.1
    return (lam, f)

star = 'HD16608'
plt.style.use('text-sans')
fig = plt.figure(figsize=(2,2))
ax = fig.add_subplot(111)
ax.set_xlabel(r'$\lambda$ [nm]')
ax.set_ylabel(r'$F_\lambda$ (norm. units)')
ax.set_ylim(0.25,0.95)
ax.set_xlim(426,442)
ax.set_xticks([428,434,440])
ax.set_yticks([0.3,0.5,0.7,0.9])
lam, f = get_spectra(star)
ax.plot(lam,f,color='black')
plt.savefig('single-line.pdf',format='pdf',bbox_inches='tight')
