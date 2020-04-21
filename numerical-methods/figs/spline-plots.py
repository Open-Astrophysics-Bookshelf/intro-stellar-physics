import numpy as np
from scipy.interpolate import CubicSpline

# colors
from matplotlib.colors import hsv_to_rgb
Ivory=hsv_to_rgb((47/360,0.06,1.00))
Red = hsv_to_rgb((14/360,1.00,0.85))
LightGreyGreen = hsv_to_rgb((150/360,0.24,0.66))
DarkerGreen = hsv_to_rgb((170/360,0.84,0.38))
DarkGreyBlue = hsv_to_rgb((193/360,0.87,0.21))

def f(x):
    return 0.5*np.cos(2.0*np.pi*x)

def fp(x):
    return -np.pi*np.sin(2.0*np.pi*x)

def eval_spline(x,xp,yp,k,include_derivatives=False):
    """
    Evaluates a cubic spline constructed between xp,yp =(x0,y0) and (x1,y1) 
    with derivatives k = (yp0,yp1) at point x
    """
    Delta = xp[1]-xp[0]
    D = (yp[1]-yp[0])/Delta
    xi = (x-xp[0])/Delta
    omxi = 1.0-xi
    s = omxi*yp[0] + xi*yp[1] + Delta*xi*omxi*(omxi*(k[0]-D)-xi*(k[1]-D))
    if not include_derivatives:
        return s
    else:
        sd = 6*xi*omxi*D + k[0]*(1.0-4*xi+3*xi**2) + k[1]*(3*xi**2 - 2*xi)
        sdd = 2.0/Delta * (3*(1-2*xi)*D + k[0]*(3*xi-2) + k[1]*(3*xi-1))
        return s, sd, sdd

def solve_tridiagonal(a,b,c,d):
    n = d.size
    x = np.zeros(n)
    for i in range(1,n):
        w = a[i]/b[i-1]
        b[i] -= w*c[i-1]
        d[i] -= w*d[i-1]
        a[i] = 0
    x[-1] = d[-1]/b[-1]
    for i in range(n-2,-1,-1):
        x[i] = (d[i]-c[i]*x[i+1])/b[i]
    return x

def plot_tangent(ax,x,y,m,loc='center',length=0.1,include_point=True,color=Red,linestyle='--'):
    xleft, xright = ax.get_xlim()
    ybottom, ytop = ax.get_ylim()
    dx = length/np.sqrt(1+m**2)
    dy = m*dx
    if loc == 'left':
        xl = x
        xr = x+dx
        yl = y
        yr = yl+dy
    elif loc == 'right':
        xl = x-dx
        xr = x
        yl = y-dy
        yr = y
    elif loc == 'center':
        xl = x-dx
        xr = x+dx
        yl = y-dy
        yr = y+dy
    else:
        raise ValueError('invalid value {0} for loc'.format(side))   
    ax.plot([xl,xr],[yl,yr],color=color,linestyle=linestyle,linewidth=0.5)
    if include_point:
        ax.plot(x,y,linestyle='none',marker='o',markersize=4,color=color)
    return ax

def layout_plot(ax):
    ax.spines['left'].set_position(('outward',10))
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('outward',10))
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_aspect('equal')
    return ax

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from matplotlib import rc
    rc('axes',titlesize='medium')
    plt.style.use('text-sans')
    alpha_min = 0.3
    alpha_max = 1.0
    xl = 0.0; xr = 0.6
    xp = np.array([xl,xr])
    yp = f(xp)
    kp = fp(xp)
    x = np.linspace(xl,xr,100)
    
    # plot different slopes at xr
    fig = plt.figure(figsize=(2,3))
    ax = fig.add_subplot(111)
    ax = layout_plot(ax)
    Nslopes = 4
    slopes = np.linspace(-kp[1],kp[1],Nslopes)
    alpha = np.linspace(alpha_min,alpha_max,Nslopes)
    for m, a in zip(slopes,alpha):
        k = np.array([kp[0],m])
        spline = eval_spline(x,xp,yp,k)
        ax.plot(x,spline,linestyle='-',alpha=a,color=DarkGreyBlue)
        ax = plot_tangent(ax,xp[1],yp[1],m,loc='right',length=0.25,include_point=False)
    ax = plot_tangent(ax,xp[0],yp[0],kp[0],loc='left',length=0.25,include_point=False)
    ax.xaxis.set_ticks(xp)
    ax.xaxis.set_ticklabels([r'$x_0$',r'$x_1$'])
    ax.yaxis.set_ticks(yp)
    ax.yaxis.set_ticklabels([r'$y_0$',r'$y_1$'])
    fig.savefig('spline-1.pdf',format='pdf',bbox_inches='tight')
    
    # make two splines connected at x = 0.3
    xm = 0.3
    # get the natural slope at xm
    s,sd,sdd = eval_spline(xm,xp,yp,kp,include_derivatives=True)
    xp = np.zeros(shape=(2,2))
    xp[0,:] = [xl,xm]
    xp[1,:] = [xm,xr]
    yp = f(xp)
    kp = np.array([kp[0],sd,kp[1]])
    x = np.zeros(shape=(2,50))
    x[0,:] = np.linspace(xl,xm,50)
    x[1,:] = np.linspace(xm,xr,50)
    
    fig = plt.figure(figsize=(2,3.4))
    ax = fig.add_subplot(111)
    ax = layout_plot(ax)
    Nslopes = 9
    slopes = np.linspace(-3.8*kp[1],4.0*kp[1],Nslopes)
    slopes[5] = kp[1]
    print('{0:6}    {1:6}'.format('D2 (L)','D2 (R)'))
    print(6*'-'+'    '+6*'-')
    left_D2 = np.zeros(shape=(Nslopes,50))
    right_D2 = np.zeros(shape=(Nslopes,50))
    for i,m in enumerate(slopes):
        if m < kp[1]:
            c = Red
            lw = 0.5
        elif m == kp[1]:
            c = DarkGreyBlue
            lw = 1.0
        else:
            c = DarkerGreen
            lw = 0.5
        if i == 4: ls = ':'
        elif i == 6: ls = '--'
        else: ls = '-'
        k = np.array([kp[0],m])
        spline,d1l,d2l = eval_spline(x[0,:],xp[0,:],yp[0,:],k,include_derivatives=True)
        left_D2[i,:] = d2l
        ax.plot(x[0,:],spline,linestyle=ls,linewidth=lw,color=c)
        k = np.array([m,kp[2]])
        spline,d1r,d2r = eval_spline(x[1,:],xp[1,:],yp[1,:],k,include_derivatives=True)
        right_D2[i,:] = d2r
        print('{0:6.2f}    {1:6.2f}'.format(d2l[-1],d2r[0]))
        ax.plot(x[1,:],spline,linestyle=ls,linewidth=lw,color=c)
    ax.xaxis.set_ticks([xl,xm,xr])
    ax.xaxis.set_ticklabels([r'$x_0$',r'$x_1$',r'$x_2$'])
    ax.yaxis.set_ticks([yp[0,0],yp[0,1],yp[1,1]])
    ax.yaxis.set_ticklabels([r'$y_0$',r'$y_1$',r'$y_2$'])
    fig.savefig('spline-2.pdf',format='pdf',bbox_inches='tight')
    
    fig = plt.figure(figsize=(2,2))
    ax = fig.add_subplot(111)
    ax = layout_plot(ax)
    ax.set_aspect('auto')
    for i,c,ls in zip([4,5,6],[DarkerGreen,DarkGreyBlue,Red],[':','-','--']):
        ax.plot(x[0,:],left_D2[i,:],linestyle=ls,linewidth=1,color=c)
        ax.plot(x[0,-1],left_D2[i,-1],marker='o',markeredgecolor=c,markerfacecolor='none',\
            markersize=4,markeredgewidth=0.5)
        ax.plot(x[1,:],right_D2[i,:],linestyle=ls,linewidth=1,color=c)
        ax.plot(x[1,0],right_D2[i,0],marker='o',markeredgecolor=c,markerfacecolor='none',markersize=4,\
            markeredgewidth=0.5)
    ax.xaxis.set_ticks([xl,xm,xr])
    ax.xaxis.set_ticklabels([r'$x_0$',r'$x_1$',r'$x_2$'])
    ax.yaxis.set_ticks(left_D2[4:7,-1])
    ax.yaxis.set_ticklabels('')
    ax.set_ylabel(r'$q^{\prime\prime}(x)$')
    fig.savefig('spline-3.pdf',format='pdf',bbox_inches='tight')
    
    fig = plt.figure(figsize=(2,2))
    ax = fig.add_subplot(111)
    ax = layout_plot(ax)
    ax.set_aspect('auto')
    xp = np.linspace(0.0,1.0,5)
    x = np.linspace(0.0,1.0,100)
    yp = f(xp)
    cs = CubicSpline(xp,yp,bc_type='natural')
    ax.plot(x,cs(x),linestyle='-',color=DarkGreyBlue)
    ax.plot(x,f(x),linestyle=':',color=LightGreyGreen)
    ax.plot(xp,yp,marker='o',color=Red,linestyle='none',markersize=4)
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$\cos(2\pi x),\,q(x)$')
    fig.savefig('spline-4.pdf',format='pdf',bbox_inches='tight')
