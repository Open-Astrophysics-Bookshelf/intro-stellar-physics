import numpy as np
from matplotlib.colors import hsv_to_rgb

# colors
Ivory=hsv_to_rgb((47/360,0.06,1.00))
Red = hsv_to_rgb((14/360,1.00,0.85))
LightGreyGreen = hsv_to_rgb((150/360,0.24,0.66))
DarkerGreen = hsv_to_rgb((170/360,0.84,0.38))
DarkGreyBlue = hsv_to_rgb((193/360,0.87,0.21))

def f(x):
    return np.sin(x)

def bisect(f,a,b):
    fa = f(a) # left side of bracket
    fb = f(b) # right side of bracket
    # orient so that f(a) < 0
    if fb < fa:
        a, b = b, a
    m = (a+b)/2
    if (f(m) < 0):
        a = m
    else:
        b = m
    return a, b

def inverse_quad(f,r,a,b):
    """
    Performs inverse quadratic interpolation to predict x s.t. f(x) = 0 in the interval
    a < x < b.
    
    on the 
    three points (r, f(r)), (a, f(a)), and (b, f(b)) to predict x s.t. f(x)=0.
    
    Arguments
        f
            function for which we seek the root f(x) = 0
        r
            guess for the root: a < r < b
        a, b
            endpoints of interval
    Returns
        x
            prediction for the root
    """
    fa = f(a)
    fb = f(b)
    fr = f(r)
    fba = fb-fa
    fra = fr-fa
    frb = fr-fb
    
    return fb*fr*a/fba/fra - fa*fr*b/fba/frb + fa*fb*r/fra/frb

def quadfit(x,y):
    """
    Given 3 points, find a parabola y = ax^2 + bx + c going through 
    the points and return the coefficients a,b,c.
    
    Arguments
        x, y (arrays)
            x and y values of the points. Should be in order x[0] < x[1] < x[2].
    Returns
        a, b, c
            coefficients of parabola y = ax^2 + bx +c
    """
    try:
        a = ((y[2]-y[0])/(x[2]-x[0]) - (y[1]-y[0])/(x[1]-x[0]))/(x[2]-x[1])
        b = (y[1]-y[0])/(x[1]-x[0]) - (x[1]+x[0])*a
        c = y[0] - a*x[0]**2 - b*x[0]
    except:
        raise ValueError('unable to compute a, b, c')
    return (a,b,c)

def base_plot(ax,x,y,color=LightGreyGreen,linewidth=0.5):
    '''
    Parameters
        ax
            axis instance
        t,z (1-dim arrays)
            solution variables
    '''
    ax.plot(x,y,color=color,linewidth=linewidth)
    ax.spines['left'].set_position(('outward',10))
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('outward',10))
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.vlines(np.pi,y.min(),y.max(),linestyle='-',linewidth=0.5,color=LightGreyGreen)
    ax.hlines(0,x.min(),x.max(),linestyle='-',linewidth=0.5,color=LightGreyGreen)
    return ax

if __name__=='__main__':
    import matplotlib.pyplot as plt
    from matplotlib import rc
    
    # set up plot stzle
    plt.style.use('text-sans')
    rc('axes',titlesize='medium')

    xguess = np.zeros(4)

    rt = np.pi
    xl = 1.5
    xr = 4.0
    xm = 0.5*(xl+xr)
    xpts = np.array([xl,xm,xr])
    ypts = f(xpts)
    x = np.linspace(xl,xr,100)
    y = f(x)
    fig = plt.figure(figsize=(2,2))
    ax = fig.add_subplot(111)
    ax = base_plot(ax,x,y,color=DarkGreyBlue,linewidth=1.0)
    a,b,c = quadfit(ypts,xpts)
    xquad = a*y**2 + b*y + c
    ax.plot(xpts,ypts,color=DarkGreyBlue,linestyle='none',marker='o')
    ax.plot(xquad,y,color=DarkerGreen,linestyle=':',linewidth=0.5)
    r = inverse_quad(f,xm,xl,xr)
    ax.plot(r,f(r),color=Red,marker='o')
    ax.vlines(r,f(r),0.0,color=Red,linestyle=':',linewidth=0.5)
    xtks = np.array([xl,xm,rt,r,xr])
    ytks = f(xtks)
    ax.xaxis.set_ticks(xtks)
    ax.xaxis.set_ticklabels([r'$a$',r'$m$',r'$r$',r'$g$',r'$b$'])
    ax.yaxis.set_ticks(ytks)
    ax.yaxis.set_ticklabels([r'$f(a)$',r'$f(m)$',r'0',r'$f(g)$',r'$f(b)$'])    
    fig.savefig('brent-1.pdf',format='pdf',bbox_inches='tight')
    
    fig = plt.figure(figsize=(2,2))
    ax = fig.add_subplot(111)
    xpts = np.array([xm,r,xr])
    ypts = f(xpts)
    ax = base_plot(ax,x,y,color=DarkGreyBlue,linewidth=1.0)
    a,b,c = quadfit(ypts,xpts)
    xquad = a*y**2 + b*y + c
    ax.plot(xpts,ypts,color=DarkGreyBlue,linestyle='none',marker='o')
    ax.plot(xquad,y,color=DarkerGreen,linestyle=':',linewidth=0.5)
    g = r
    r = inverse_quad(f,g,xm,xr)
    ax.plot(r,f(r),color=Red,marker='o')
    xtks = np.array([xm,r,g,xr])
    ytks = f(xtks)
    ax.xaxis.set_ticks(xtks)
    ax.xaxis.set_ticklabels([r'$m$',r'$r$',r'$g$',r'$b$'])
    ax.yaxis.set_ticks(ytks)
    ax.yaxis.set_ticklabels([r'$f(m)$',r'0',r'$f(g)$',r'$f(b)$'])    
    fig.savefig('brent-2.pdf',format='pdf',bbox_inches='tight')    
    