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

def secant(f,a,b):
    """
    Constructs secant to approximate root of f on a,b
    """
    fa = f(a)
    fb = f(b)
    if fa*fb >= 0.0:
        raise ValueError("root not bracketed")
    return (fb*a-fa*b)/(fb-fa)

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

def brent_step(f,a,b,c,d,prev='bisection'):
    delta = 4.0*np.finfo(1.0).eps
    fa = f(a); fb = f(b); fc = f(c)
    assert(fa*fb < 0)
    assert(np.abs(fb) < np.abs(fa))
    # propose a step
    method = 'secant'
    if (fa != fc) and (fb != fc):
        s = inverse_quad(f,c,a,b)
        method = 'inverse quadratic'
    else:
        s = secant(f,a,b)
    # acceptance conditions
    if (s > (3*a+b)/4 and s < b) or (s < (3*a+b)/4 and s > b):
        if prev == 'bisection':
            if np.abs(s-b) >= 0.5*np.abs(b-c) and np.abs(b-c) < delta:
                s = 0.5*(a+b)
                method = 'bisection'
        else:
            if np.abs(s-b) >= 0.5*np.abs(c-d) and np.abs(c-d) < delta:
                s = 0.5*(a+b)
                method = 'bisection'
    else:
        s = 0.5*(a+b)
        method = 'bisection'
    fs = f(s)
    # set b[k-2] = b[k-1], b[k-1] = b[k]
    d = c
    c = b
    # set b[k] based on sign of f(s) so that root remains bracketed
    if fa*fs < 0:
        # root lies between a, s so set b = s
        b = s
        fb = fs
    else:
        # root lies between s, b so move a to s
        a = s
        fa = fs
    # keep b closer to root
    if np.abs(fa) < np.abs(fb):
        a,b = b,a
    
    return (a, b, c, d, s, method)
    
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

def sequence_plots(xleft,xright,Nsteps,basename='brent'):
    rt = np.pi
    x = np.linspace(xleft,xright,100)
    y = f(x)
    a = xleft; b = xright; c = a; d = 0.0
    fa = f(a); fb = f(b)
    assert(fa*fb < 0.0)
    if np.abs(fa) < np.abs(fb):
        a, b = b, a
    for step in range(Nsteps):
        print('step {0}'.format(step))
        plotname = '{0}-{1:0d}.pdf'.format(basename,step)
        fig = plt.figure(figsize=(2,2))
        ax = fig.add_subplot(111)
        ax = base_plot(ax,x,y,color=DarkGreyBlue,linewidth=1)
        ax.plot([a,b],[f(a),f(b)],color=DarkGreyBlue,linestyle='none',marker='o',markersize=4)
        xtks = [a,b]
        ytks = [f(a),f(b)]
        xlabs = [r'$a$',r'$b$']
        ylabs = [r'$f(a)$',r'$f(b)$']
        if c != a and c != b:
            ax.plot(c,f(c),color=DarkGreyBlue,marker='o',markersize=4)
            xtks += [c]
            xlabs += [r'$c$']
            ytks += [f(c)]
            ylabs += [r'$f(c)$']
        aa = a; bb = b; cc = c
        fa = f(a); fb = f(b); fc = f(c)
        a,b,c,d,s,method = brent_step(f,a,b,c,d)
        print('method = {0}, s = {1:5.2f}'.format(method,s))
        print('a, b, c, d = '+' '.join(['{0:5.2f}'.format(i) for i in (a,b,c,d)]))
        ax.plot(s,f(s),color=Red,marker='o',markersize=4)
        xtks += [s]
        ytks += [f(s)]
        if method != 'bisection':
            xlabs += [r'$s$']
            ylabs += [r'$f(s)$']
        else:
            xlabs += [r'$m$']
            ylabs += [r'$f(m)$']            
        # options
        if method == 'secant':
            ax.plot([aa,bb],[f(aa),f(bb)],color=Red,linestyle=':',linewidth=0.5)
        elif method == 'inverse quadratic':
            ypts = np.array([fa,fb,fc])
            xpts = np.array([aa,bb,cc])
            isort = np.argsort(ypts)
            qa,qb,qc = quadfit(ypts[isort],xpts[isort])
            yquad = np.linspace(y.min(),y.max(),50)
            xquad = qa*yquad**2+qb*yquad+qc
            ax.plot(xquad,yquad,color=Red,linestyle=':',linewidth=0.5)
        ax.xaxis.set_ticks(xtks)
        ax.xaxis.set_ticklabels(xlabs)
        ax.yaxis.set_ticks(ytks)
        ax.yaxis.set_ticklabels(ylabs)
        fig.savefig(plotname,format='pdf',bbox_inches='tight')
    
if __name__=='__main__':
    import matplotlib.pyplot as plt
    from matplotlib import rc
    
    # set up plot stzle
    plt.style.use('text-sans')
    rc('axes',titlesize='medium')

    xl = 1.6
    xr = 5.1
    sequence_plots(xl,xr,3)

    xl = 1.4
    xr = 5.9
    sequence_plots(xl,xr,3,basename='trial')
