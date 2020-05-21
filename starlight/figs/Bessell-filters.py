
# coding: utf-8

# # Bessell UBVRI Filters
# 
# From Bessell 1990, PASP 102, 1181
# Digital tables courtesy Michael Richmod (Rochester Institute of Technology

from __future__ import print_function, division
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
# get_ipython().magic(u'matplotlib inline')


# ## Filters
# 
# Arrays are wavelength (Å) and transmission coefficient.

U = np.array(
    [[3000,0.00],
    [3050,0.016],
    [3100,0.068],
    [3150,0.167],
    [3200,0.287],
    [3250,0.423],
    [3300,0.560],
    [3350,0.673],
    [3400,0.772],
    [3450,0.841],
    [3500,0.905],
    [3550,0.943],
    [3600,0.981],
    [3650,0.993],
    [3700,1.000],
    [3750,0.989],
    [3800,0.916],
    [3850,0.804],
    [3900,0.625],
    [3950,0.423],
    [4000,0.238],
    [4050,0.114],
    [4100,0.051],
    [4150,0.019],
    [4200,0.000]])


B = np.array([
    [3600,0.0],
    [3700,0.030],
    [3800,0.134],
    [3900,0.567],
    [4000,0.920],
    [4100,0.978],
    [4200,1.000],
    [4300,0.978],
    [4400,0.935],
    [4500,0.853],
    [4600,0.740],
    [4700,0.640],
    [4800,0.536],
    [4900,0.424],
    [5000,0.325],
    [5100,0.235],
    [5200,0.150],
    [5300,0.095],
    [5400,0.043],
    [5500,0.009],
    [5600,0.0]
    ])


V = np.array([
    [4700,0.000],
    [4800,0.030],
    [4900,0.163],
    [5000,0.458],
    [5100,0.780],
    [5200,0.967],
    [5300,1.000],
    [5400,0.973],
    [5500,0.898],
    [5600,0.792],
    [5700,0.684],
    [5800,0.574],
    [5900,0.461],
    [6000,0.359],
    [6100,0.270],
    [6200,0.197],
    [6300,0.135],
    [6400,0.081],
    [6500,0.045],
    [6600,0.025],
    [6700,0.017],
    [6800,0.013],
    [6900,0.009],
    [7000,0.000]
    ])


R = np.array([
    [5500,0.000],
    [5600,0.23],
    [5700,0.74],
    [5800,0.91],
    [5900,0.98],
    [6000,1.000],
    [6100,0.98],
    [6200,0.96],
    [6300,0.93],
    [6400,0.90],
    [6500,0.86],
    [6600,0.81],
    [6700,0.78],
    [6800,0.72],
    [6900,0.67],
    [7000,0.61],
    [7100,0.56],
    [7200,0.51],
    [7300,0.46],
    [7400,0.40],
    [7500,0.35],
    [8000,0.14],
    [8500,0.03],
    [9000,0.00]
    ])


I = np.array([
    [7000,0.000],
    [7100,0.024],
    [7200,0.232],
    [7300,0.555],
    [7400,0.785],
    [7500,0.910],
    [7600,0.965],
    [7700,0.985],
    [7800,0.990],
    [7900,0.995],
    [8000,1.000],
    [8100,1.000],
    [8200,0.990],
    [8300,0.980],
    [8400,0.950],
    [8500,0.910],
    [8600,0.860],
    [8700,0.750],
    [8800,0.560],
    [8900,0.330],
    [9000,0.150],
    [9100,0.030],
    [9200,0.000]
    ])


# Next we scale the wavelengths to nm.

A_to_nm = np.array([0.1,1.0])

U = U*A_to_nm
B = B*A_to_nm
V = V*A_to_nm
R = R*A_to_nm
I = I*A_to_nm


# ## Set up the plot
xmin, xmax, ymin, ymax = 300,920,0.0,1.1

from matplotlib.colors import hsv_to_rgb
red = hsv_to_rgb((14/360,1,0.85))
light_cream = hsv_to_rgb((47/360,0.06,1.00))
heavy_cream = hsv_to_rgb((47/360,0.24,1.00))
light_grey_green = hsv_to_rgb((150/360,0.24,0.66))
darker_green = hsv_to_rgb((170/360,0.84,0.38))
dark_grey_blue = hsv_to_rgb((193/360,0.87,0.21))


charsize=14
major_ticklength=0.6*charsize
major_tickwidth=0.9
minor_ticklength=0.3*charsize
minor_tickwidth=0.7
rc('figure',**{'figsize':(8,5),'facecolor':'none'})
rc('mathtext',**{'fontset':'stixsans'})
rc('font',**{'family':'sans-serif','size':charsize})
rc('axes',**{'titlesize':charsize,'labelsize':charsize,'facecolor':'none','edgecolor':dark_grey_blue,
             'labelcolor':dark_grey_blue})
rc('xtick',**{'major.size':major_ticklength,'major.width':major_tickwidth,'labelsize':'small','direction':'out',
             'color':dark_grey_blue})
rc('ytick',**{'major.size':major_ticklength,'major.width':major_tickwidth,'labelsize':'small','direction':'out',
             'color':dark_grey_blue})
rc('lines',**{'linewidth':1.5,'dash_capstyle':'round','color':dark_grey_blue})
rc('text',**{'color':dark_grey_blue})


plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
plt.xlabel(r'$\lambda/\mathrm{nm}$')
plt.ylabel(r'$\mathcal{T}(\lambda)$')
plt.plot(U[:,0],U[:,1],'0.3')
plt.plot(B[:,0],B[:,1],'0.3')
plt.plot(V[:,0],V[:,1],'0.3')
plt.plot(R[:,0],R[:,1],'0.3')
plt.plot(I[:,0],I[:,1],'0.3')
for lab,fil in zip(['U','B','V','R','I'],[U,B,V,R,I]):
    xloc = fil[np.where(fil[:,1]==1.0),0][0,0]
    yloc = 0.8
    plt.annotate(s=lab,xy=(xloc,yloc),ha='center',va='center')
plt.savefig('UBVRI.pdf',format='pdf')


import scipy.constants as sc

def planck(lam,T):
    '''
    lam := wavelength [nm]
    T := temperature [K]
    '''
    l= lam*1.0e-9
    return 2*sc.h*sc.c**2/l**5 / (np.exp(sc.h*sc.c/l/sc.k/T) - 1)


B_FWHM = B[np.where(B[:,1] > 0.5),0]
Bmin = B_FWHM.min()
Bmax = B_FWHM.max()
V_FWHM = V[np.where(V[:,1]>0.5),0]
Vmin = V_FWHM.min()
Vmax = V_FWHM.max()

lam = np.linspace(xmin,xmax,512)
Bsun = planck(lam,5800)
Bhot = planck(lam,8000)
Bsun /= Bsun.max()
Bhot /= Bhot.max()

fig,(ax2,ax1) = plt.subplots(2,1,sharex='all')
plt.subplots_adjust(hspace=0.001)
plt.xlim(xmin,xmax)
ax1.set_ylim(ymin,ymax)
ax1.set_xlabel(r'$\lambda/\mathrm{nm}$')
ax1.set_ylabel(r'$B_\lambda/\max(B_\lambda)$')
ax1.plot(lam,Bsun,'0.3')
ax1.fill_between(lam,Bsun,where=((lam-Bmin)*(Bmax-lam)>0.0),color=darker_green)
ax1.fill_between(lam,Bsun,where=((lam-Vmin)*(Vmax-lam)>0.0),color=light_grey_green)
for lab,fil in zip(['B','V'],[B,V]):
    xloc = fil[np.where(fil[:,1]==1.0),0][0,0]
    yloc = 0.6
    ax1.annotate(s=lab,xy=(xloc,yloc),ha='center',va='center',color=heavy_cream)
ax1.annotate(s=r'$T = 5800\,\mathrm{K}$',xy=(800,0.8),size='small',ha='left')

ax2.set_ylim(ymin,ymax)
ax2.set_ylabel(r'$B_\lambda/\max(B_\lambda)$')
ax2.plot(lam,Bhot/Bhot.max(),'0.3')
ax2.fill_between(lam,Bhot,where=((lam-Bmin)*(Bmax-lam)>0.0),color=darker_green)
ax2.fill_between(lam,Bhot,where=((lam-Vmin)*(Vmax-lam)>0.0),color=light_grey_green)
for lab,fil in zip(['B','V'],[B,V]):
    xloc = fil[np.where(fil[:,1]==1.0),0][0,0]
    yloc = 0.6
    ax2.annotate(s=lab,xy=(xloc,yloc),ha='center',va='center',color=heavy_cream)
ax2.annotate(s=r'$T = 8000\,\mathrm{K}$',xy=(800,0.8),size='small',ha='left')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.savefig('B-V.pdf',format='pdf')
