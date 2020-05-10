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

def base_plot(ax,x,y,xl,xr,color=LightGreyGreen,linewidth=0.5):
    '''
    Parameters
        ax
            axis instance
        t,z (1-dim arrays)
            solution variables
    '''
    xm = 0.5*(xl+xr)
    rt = np.pi
    xtks = np.array([xl,xm,rt,xr])
    ytks = f(xtks)
    ax.plot(x,y,color=color,linewidth=linewidth)
    ax.spines['left'].set_position(('outward',10))
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('outward',10))
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks(xtks)
    ax.yaxis.set_ticks(ytks)
    ax.xaxis.set_ticklabels([r'$a$',r'$m$',r'$r$',r'$b$'])
    ax.yaxis.set_ticklabels([r'$f(a)$',r'$f(m)$','0',r'$f(b)$'])
    ax.vlines(np.pi,y.min(),y.max(),linestyle='-',linewidth=0.5,color=LightGreyGreen)
    ax.hlines(0,x.min(),x.max(),linestyle='-',linewidth=0.5,color=LightGreyGreen)
    return ax

def plot_points(ax,xl,xr,func):
    xm = 0.5*(xl+xr)
    xpts = np.array([xl,xr])
    ypts = func(xpts)
    ym = func(xm)
    ax.plot(xpts,ypts,marker='o',color=DarkGreyBlue,linestyle='none')
    ax.plot(xm,ym,marker='o',color=Red)
    return ax

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from matplotlib import rc
    
    # set up plot stzle
    plt.style.use('text-sans')
    rc('axes',titlesize='medium')

    xguess = np.zeros(4)

    xl = 1.5
    xr = 4.0
    x = np.linspace(xl,xr,100)
    y = f(x)
    fig = plt.figure(figsize=(2,2))
    ax = fig.add_subplot(111)
    ax = base_plot(ax,x,y,xl,xr,color=DarkGreyBlue,linewidth=1.0)
    ax = plot_points(ax,xl,xr,f)
    ax.set_title('First bisection')
    fig.savefig('bisection-1.pdf',format='pdf',bbox_inches='tight')
    
    xl,xr = bisect(f,xl,xr)
    xguess[1] = 0.5*(xl+xr)
    fig = plt.figure(figsize=(2,2))
    ax = fig.add_subplot(111)
    ax = base_plot(ax,x,y,xr,xl,color=DarkGreyBlue,linewidth=1.0)
    ax = plot_points(ax,xl,xr,f)
    ax.set_title('Second bisection')
    fig.savefig('bisection-2.pdf',format='pdf',bbox_inches='tight')
        
    fig = plt.figure(figsize=(2,2))
    ax = fig.add_subplot(111)
    xl = 1.5
    xr = 4.0
    ax = base_plot(ax,x,y,xl,xr,color=DarkGreyBlue,linewidth=1.0)
    ax.xaxis.set_ticks([xl,np.pi,xr])
    ax.xaxis.set_ticklabels([r'$a$',r'$r$',r'$b$'])
    ax.yaxis.set_ticks([f(xl),f(np.pi),f(xr)])
    ax.yaxis.set_ticklabels([r'$f(a)$','0',r'$f(b)$'])
    for i in range(5):
        r = 0.5*(xl+xr)
        ax.plot(r,f(r),linestyle='none',marker='o',color=Red,markersize=4)
        plt.annotate(s='{0:d}'.format(i+1),xy=(r,f(r)),\
            va='bottom',ha='left',xytext=(4,4),textcoords='offset points',size='x-small',color=Red)
        xl, xr = bisect(f,xl,xr)
    ax.set_title('First 5 bisections')
    fig.savefig('bisection-3.pdf',format='pdf',bbox_inches='tight')
    