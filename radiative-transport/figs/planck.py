"""
Plot of Planck spectra and a sample opacity kappa_nu
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse

class spectral_line: 
    def __init__(self,loc=0.0,fwhm=1.0):
        self._nu0 = loc
        self._fwhm = fwhm
        self._Gamma = 2*np.pi*fwhm

    def profile(self,nu):
        d2 = (nu-self._nu0)**2
        g4pi = self._Gamma/4.0/np.pi
        return (1.0/np.pi)*g4pi/(d2 + g4pi**2)

    @property
    def FWHM(self):
        return self._fwhm

    @FWHM.setter
    def FWHM(self,fwhm=1.0):
        self._Gamma = 2*np.pi*fwhm
        self._fwhm = fwhm

    @property
    def center(self):
        return self._nu0

    @center.setter
    def center(self,loc=0.0):
        self._nu0 = loc


def Bnu(x):
    return x**3/(np.exp(x)-1.0)

def dBnu(x):
    return x**4 * np.exp(x)/(np.exp(x)-1.0)**2

def knu(x):
    l0 = spectral_line(2.8,0.08)
    l1 = spectral_line(3.8,0.08)
    raw =  10.0 - l0.profile(x) - l1.profile(x) + 4.0*np.tanh((x-4.5)/0.5)
    norm = np.max(raw)-np.min(raw)
    return 5.0*(1.0+raw/norm)

def Fnu(x):
    db = dBnu(x)
    k = knu(x)
    db /= np.max(db)
    k /= np.min(k)
    f = db/k
    return f

if __name__ == '__main__':

    opts = argparse.ArgumentParser()
    opts.add_argument(
        "-s","--solution",
        action="store_true",default=False,
        help="draw the plot with solution")
    opts.add_argument(
        "-o","--output-file",
        nargs=1,default="planck.pdf",
        help="name for output file"
    )
    
    solution = opts.parse_args().solution
    pltname = opts.parse_args().output_file[0]
        
    plt.style.use('text-sans')
    plt.rc('font',**{'size':9})
    plt.rc('grid',**{'color':'lightgrey','linestyle':'-'})
    plt.rc('axes',**{'axisbelow':True})
    
    xlim = (2.5,5.05)
    x = np.linspace(*xlim,256)
    fig = plt.figure(figsize=(2,3))
    p = fig.add_subplot(3,1,1)
    p.set_ylabel(r'$B_\nu$, $dB_\nu\,/dT$')
    p.set_xlim(xlim)
    p.set_ylim(0.55,1.15)
    p.grid(True)
    p.minorticks_on()
    p.axes.xaxis.set_ticklabels([])
    b = Bnu(x)
    b /= np.max(b)
    db = dBnu(x)
    db /= np.max(db)
    p.plot(x,b,'k-',x,db,'k--')
    xlab = 4.25
    xind = np.where(x > xlab)
    blab = b[xind][0]
    dblab = db[xind][0]
    p.annotate(xy=(xlab,blab),s=r'$B_\nu$',size='small',ha='left',va='bottom')
    p.annotate(xy=(xlab,dblab),s=r'$dB_\nu\,/dT$',size='small',
        ha='left',va='bottom')
    
    f = fig.add_subplot(3,1,2)
    f.set_xlim(xlim)
    f.set_ylim(0.9,2.2)
    f.set_ylabel(r'$\kappa_\nu$')
    f.axes.xaxis.set_ticklabels([])
    f.grid(True)
    f.minorticks_on()
    k = knu(x)
    k /= np.min(k)
    f.plot(x,k,'k-')

    u = fig.add_subplot(3,1,3)
    u.set_xlim(xlim)
    u.set_ylim(0.4,1.0)
    u.set_ylabel(r'$F_\nu$')
    u.set_xlabel(r'$h\nu\,/kT$')
    u.grid(True)
    u.minorticks_on()
    if solution:
        u.plot(x,Fnu(x),'r-')
    
    if solution:
        pltname += '-solution'

    plt.savefig(pltname+'.pdf',format='pdf',bbox_inches='tight')
