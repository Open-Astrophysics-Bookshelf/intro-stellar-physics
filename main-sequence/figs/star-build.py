import numpy as np
import matplotlib.pyplot as plt
import argparse
import scipy.constants as sc

def load_mesa_results():
    mesa_data='''\
    0.09  5.70  6.60
    0.15  5.35  6.75
    0.30  5.00  6.87
    2.0  4.80  7.30
    10.0  4.00  7.50
    25.0  3.60  7.55
    100.0  3.25  7.63'''

    mass = []
    lgrho = []
    lgT = []

    for row in mesa_data.split('\n'):
    	data = row.split()
    	mass.append(data[0])
    	lgrho.append(float(data[1]))
    	lgT.append(float(data[2]))
    
    return mass,lgrho,lgT

def set_composition_moments(composition):
    Nisos = len(composition)
    X = np.zeros(Nisos)
    Z = np.zeros(Nisos)
    A = np.zeros(Nisos)
    for i, iso in enumerate(composition):
        Z[i],A[i],X[i] = composition[iso]

    mu = 1.0/(np.sum(X*(1.0+Z)/A))
    mue = 1.0/(np.sum(X*Z/A))
    mui = 1.0/(np.sum(X/A))
    return mu,mue,mui

def Fermi_energy(rho,mue):
    return 0.5*sc.h**2/sc.m_e*(3*rho/mue/sc.m_u/8/sc.pi)**(2/3)

def degeneracy_threshold_temperature(rho,mue,fac=1):
    return (1/fac)*Fermi_energy(rho,mue)/sc.k
    
def radiation_threshold_temperature(rho,mu):
    arad = 4*sc.sigma/sc.c
    return (3*rho/mu/sc.m_u/arad*sc.k)**(1/3)

def contraction_temperature(lgTZAMS,lgrhoZAMS,lgrho):
    lgT = (lgrho-lgrhoZAMS)/3 + lgTZAMS
    contraction = np.where(lgrho < lgrhoZAMS)
    return lgrho[contraction],lgT[contraction]

if __name__ == '__main__':

    opts = argparse.ArgumentParser()
    opts.add_argument(
        "-s","--solution",
        action="store_true",default=False,
        help="draw the plot with solution")
    solution = opts.parse_args().solution

    plotname = 'rho-T-grid'
    if solution:
        plotname += '-solution'

    plt.style.use('text-sans')

    composition = {'H':(1,1,0.7),'He':(2,4,0.3)}
    mu,mue,mui = set_composition_moments(composition)

    rho_lim = (2,8) # kg/m^3
    T_lim = (5,9) # K
    rho = np.logspace(*rho_lim,100)
    star_mass,star_lgrho,star_lgT = load_mesa_results()
    
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111)
    ax.set_xlim(rho_lim)
    ax.set_xlabel(r'$\log(\rho/\mathrm{kg\,m^{-3}})$')
    ax.set_ylim(T_lim)
    ax.set_ylabel(r'$\log(T/\mathrm{K})$')
    # ax.minorticks_on()
    ax.plot(star_lgrho,star_lgT,
        marker='^',markerfacecolor='0.4',markeredgecolor='0.3',
        linestyle='none',zorder=3)
    for m, r, t in zip(star_mass,star_lgrho,star_lgT):
        ax.annotate(
            s=m,xy=(r,t),va='bottom',ha='left',size='x-small',
            xytext=(3,3),textcoords='offset points',color='0.3',rotation=np.rad2deg(np.arctan(2/3)))
    if solution:
        for m, r, t in zip(star_mass,star_lgrho,star_lgT):
            lgrho_c, lgT_c = contraction_temperature(t,r,np.log10(rho))
            npts = len(lgrho_c)
            for i in range(npts-1):
                a = max(i/(npts-1),0.1)
                ax.plot(lgrho_c[i:i+2],lgT_c[i:i+2],color='0.3',linestyle='-',
                    zorder=1,alpha=a,solid_capstyle='butt')
        for fac in (1,3,10):
            TFermi = degeneracy_threshold_temperature(rho,mue,fac)
            ax.plot(np.log10(rho),np.log10(TFermi),'k:')
            nloc = np.where(TFermi > 1e7)[0][0]
            ax.annotate(s=r'$E_{{\mathrm{{F}}}} = {0}kT$'.format(fac),
                xy=(np.log10(rho[nloc]),np.log10(TFermi[nloc])),va='bottom',
                rotation=45,xytext=(0,8),
                textcoords='offset points')
        ax.annotate(s='degenerate',xy=(7.5,5.25),ha='right')
        Trad = radiation_threshold_temperature(rho,mu)
        ax.plot(np.log10(rho),np.log10(Trad),'k--')
        nloc = np.where(Trad > 1.0e8)[0][0]
        ax.annotate(s=r'$P_{\mathrm{rad}} = P_{\mathrm{gas}}$',
            xy=(np.log10(rho[nloc]),np.log10(Trad[nloc])),va='bottom',
            rotation=np.rad2deg(np.arctan(0.5)),xytext=(0,4),
            textcoords='offset points')            
        ax.annotate(s='radiation-dominated',xy=(2.5,8.7))
    else:
        ax.grid(which='both',color='0.7',linewidth=0.3,linestyle=':')

    plt.savefig(plotname+'.pdf',format='pdf',bbox_inches='tight')
