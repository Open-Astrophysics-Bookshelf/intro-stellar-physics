import numpy as np
from matplotlib.colors import hsv_to_rgb

# colors
Ivory=hsv_to_rgb((47/360,0.06,1.00))
Red = hsv_to_rgb((14/360,1.00,0.85))
LightGreyGreen = hsv_to_rgb((150/360,0.24,0.66))
DarkerGreen = hsv_to_rgb((170/360,0.84,0.38))
DarkGreyBlue = hsv_to_rgb((193/360,0.87,0.21))

# system of ODEs and their solution
def f(t,z):
    """
    RHS of equation dz/dt = f(t,z)
    """
    # this makes an array of length 2, each element of which is zero
    dzdt = np.zeros(2)
    
    dzdt[0] = 2.0*np.pi*z[1]
    dzdt[1] = -2.0*np.pi*z[0]
    return dzdt

def sol(t):
    # this allows us to generate solution if x is a scalar
    # could probably do it better with some kind of spread function
    t = np.atleast_1d(t)
    z = np.zeros(shape=(2,t.size))
    z[0] = np.sin(2.0*np.pi*t)
    z[1] = np.cos(2.0*np.pi*t)
    return z

# various plots
def plot_solution(ax,t,z,color=LightGreyGreen,linewidth=0.5):
    '''
    Parameters
        ax
            axis instance
        t,z (1-dim arrays)
            solution variables
    '''
    # locations of ticks: left, right, and middle
    tl = t[0]
    tr = t[-1]
    tm = 0.5*(tl+tr)
    ax.plot(t,z,color=color,linewidth=linewidth)
    ax.spines['left'].set_position(('outward',10))
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('outward',10))
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xticks([tl,tm,tr])
    ax.set_xticklabels([r'$t$',r'$t+h/2$',r'$t+h$'])
    ax.set_yticks([z[0],z[-1]])
    ax.set_yticklabels([r'$z_0(t)$',r'$z_0(t+h)$'])
    return ax
    
def plot_slope(ax,t,z,k,loc='mid',length=0.02,include_point=True,color=Red):
    '''
    Parameters:
        ax
            axis instance
        t,z (scalar)
            point at which slope is to be computed
        k (scalar)
            slope
        loc
            'left', 'right', or 'mid'
        length
            distance line extends from marker in either direction
    '''
    
    # adjust the line length to prevent visual distortion due to different x-, y-scales
    tleft,tright = ax.get_xlim()
    zbottom,ztop = ax.get_ylim()
    aspect = (ztop-zbottom)/(tright-tleft)
    visual_length = length/np.sqrt(1+(k/aspect)**2)
    dt = visual_length
    dz = visual_length*k

    # slope is one sided if on the left or right side of interval
    if loc == 'left':
        tl = t
        tr = tl+dt
        zl = z
        zr = zl+dz
    elif loc == 'right':
        tl = t-dt
        tr = t
        zl = z-dz
        zr = z
    elif loc == 'mid':
        tl = t-dt
        tr = t+dt
        zl = z-dz
        zr = z+dz
    else:
        raise ValueError(loc+' is not an understood value for loc')

    ax.plot([tl,tr],[zl,zr],color=color)

    if include_point:
        ax.plot(t,z,linestyle='none',marker='o',markersize=8,color=color)
    return ax

def plot_step(ax,t,z,line_color=Red,left_marker_color=DarkerGreen,right_marker_color=Red):
    '''
    Parameters:
        ax
            axis instance
        t,z (arrays)
             step from (tl, zl) to  (tr, zr)
    '''
    # line
    ax.plot(t,z,linestyle=':',color=line_color)
    # left point marker
    ax.plot(t[0],z[0],linestyle='none',marker='o',markersize=8,color=left_marker_color)
    # right point marker
    ax.plot(t[-1],z[-1],linestyle='none',marker='o',markersize=8,color=right_marker_color)
    return ax

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from matplotlib import rc
    
    # set up plot stzle
    plt.style.use('text-sans')
    rc('axes',titlesize='medium')
    
    # parameters for schematic
    t = 0.12    # starting point
    z = np.ravel(sol(t))  # value at starting point
    h = 0.12    # step
    
    # solution of ODEs
    Npts = 40 # enough points for a smooth curve
    tsol = np.linspace(t,t+h,Npts)
    zsol = sol(tsol)
    
    print('\nsolution to ODE')
    fig = plt.figure(figsize=(2,2))
    ax = fig.add_subplot(111)
    ax = plot_solution(ax,tsol,zsol[0,:],color=DarkGreyBlue,linewidth=1)
    fig.savefig('solution.pdf',format='pdf',bbox_inches='tight')

    print('\nschematic of forward Euler')
    k = f(t,z)
    zh = z + h*k
    fig = plt.figure(figsize=(5,2.5))
    ax1 = fig.add_subplot(121)
    ax1 = plot_solution(ax1,tsol,zsol[0,:])
    ax1 = plot_slope(ax1,t,z[0],k[0],loc='left')

    ax2 = fig.add_subplot(122)
    ax2 = plot_solution(ax2,tsol,zsol[0,:])
    ax2 = plot_step(ax2,[t,t+h],[z[0],zh[0]])
    ax2.annotate(s=r'$f(t,z)$',xy=(t+0.5*h,0.5*(z[0]+zh[0])),ha='right',va='center',\
        color=Red,xytext=(-4,0),textcoords='offset points')
    fig.tight_layout()
    fig.savefig('forward-Euler.pdf',format='pdf',bbox_inches='tight')
    
    print('\nschematic of 2nd order Runge-Kutta')
    k = f(t,z)
    t_12 = t+0.5*h
    z_12 = z+0.5*h*k
    f_12 = f(t_12,z_12)
    zh = z + h*f(t_12,z_12)

    print('    step 1')
    fig = plt.figure(figsize = (5,2.5))
    ax1 = fig.add_subplot(121)
    ax1 = plot_solution(ax1,tsol,zsol[0,:])
    ax1 = plot_slope(ax1,t,z[0],k[0],loc='left')

    ax2 = fig.add_subplot(122)
    ax2 = plot_solution(ax2,tsol,zsol[0,:])
    ax2 = plot_step(ax2,[t,t_12],[z[0],z_12[0]])
    ax2.annotate(s=r'$f(t,z)$',xy=(0.5*(t+t_12),0.5*(z[0]+z_12[0])),ha='right',va='center',\
        color=Red,xytext=(-4,0),textcoords='offset points')

    fig.tight_layout()
    fig.savefig('rk2-1.pdf',format='pdf',bbox_inches='tight')
    
    print('    step 2')
    fig = plt.figure(figsize = (2.5,2.5))
    ax = fig.add_subplot(111)
    ax = plot_solution(ax,tsol,zsol[0,:])
    ax = plot_slope(ax,t_12,z_12[0],f_12[0],loc='mid')
    ax = plot_step(ax,[t,t+h],[z[0],zh[0]])
    ax.annotate(s=r'$f(t+h/2,z_{\mathrm{p}})$',xy=(t+0.5*h,0.5*(z[0]+zh[0])),ha='left',va='center',\
        color=Red,xytext=(4,-4),textcoords='offset points')

    fig.tight_layout()
    fig.savefig('rk2-2.pdf',format='pdf',bbox_inches='tight')
    
    print('\nschematic of 4th order Runge-Kutta')
    k1 = f(t,z)
    t12 = t + 0.5*h
    z12 = z + 0.5*h*k1
    k2 = f(t12,z12)
    z12p = z + 0.5*h*k2
    k3 = f(t12,z12p)
    th = t+h
    zhp = z + h*k3
    k4 = f(th,zhp)
    zh = z + (h/6)*(k1+2*k2+2*k3+k4)

    print('    step 1')
    fig = plt.figure(figsize=(5,2.5))
    ax1 = fig.add_subplot(121)
    ax1 = plot_solution(ax1,tsol,zsol[0,:])
    ax1 = plot_slope(ax1,t,z[0],k1[0],loc='left')

    ax2 = fig.add_subplot(122)
    ax2 = plot_solution(ax2,tsol,zsol[0,:])
    ax2 = plot_step(ax2,[t,t12],[z[0],z12[0]])
    ax2.annotate(s=r'$k_1$',xy=(0.5*(t+t12),0.5*(z[0]+z12[0])),ha='right',va='center',\
        color=Red,xytext=(-4,0),textcoords='offset points')

    fig.tight_layout()
    fig.savefig('rk4-1.pdf',format='pdf',bbox_inches='tight')
    
    print('    step 2')
    fig = plt.figure(figsize=(2.5,2.5))
    ax = fig.add_subplot(111)
    ax = plot_solution(ax,tsol,zsol[0,:])
    ax = plot_slope(ax,t12,z12[0],k2[0],loc='mid')
    ax = plot_step(ax,[t,t12],[z[0],z12p[0]])
    ax.annotate(s=r'$k_2$',xy=(0.5*(t+t12),0.5*(z[0]+z12p[0])),ha='left',va='center',\
        color=Red,xytext=(4,-4),textcoords='offset points')

    fig.tight_layout()
    fig.savefig('rk4-2.pdf',format='pdf',bbox_inches='tight')
    
    print('    step 3')
    fig = plt.figure(figsize=(2.5,2.5))
    ax = fig.add_subplot(111)
    ax = plot_solution(ax,tsol,zsol[0,:])
    ax = plot_slope(ax,t12,z12p[0],k3[0],loc='mid')
    ax = plot_solution(ax,tsol,zsol[0,:])
    ax = plot_step(ax,[t,th],[z[0],zhp[0]])
    ax.annotate(s=r'$k_3$',xy=(0.5*(t+th),0.5*(z[0]+zhp[0])),ha='left',va='center',\
        color=Red,xytext=(4,-4),textcoords='offset points')

    fig.tight_layout()
    fig.savefig('rk4-3.pdf',format='pdf',bbox_inches='tight')
    
    print('    step 4')
    fig = plt.figure(figsize=(5,2.5))
    ax1 = fig.add_subplot(121)
    ax1 = plot_solution(ax1,tsol,zsol[0,:])
    ax1 = plot_slope(ax1,th,zhp[0],k4[0],loc='right')

    ax2 = fig.add_subplot(122)
    ax2 = plot_solution(ax2,tsol,zsol[0,:])
    ax2 = plot_slope(ax2,t,z[0],k1[0],loc='left',length=0.02,include_point=False)
    ax2 = plot_slope(ax2,t,z[0],k2[0],loc='left',length=0.04,include_point=False)
    ax2 = plot_slope(ax2,t,z[0],k3[0],loc='left',length=0.04,include_point=False)
    ax2 = plot_slope(ax2,t,z[0],k4[0],loc='left',length=0.02,include_point=False)
    ax2 = plot_step(ax2,[t,th],[z[0],zh[0]])
    ax2.annotate(s=r'$(k_1+2k_2+2k_3+k_4)/6$',xy=(0.5*(t+th),0.5*(z[0]+zh[0])),ha='left',va='center',\
        color=Red,xytext=(4,-4),textcoords='offset points')

    fig.tight_layout()
    fig.savefig('rk4-4.pdf',format='pdf',bbox_inches='tight')
