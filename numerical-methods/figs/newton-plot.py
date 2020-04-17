import numpy as np
from matplotlib.colors import hsv_to_rgb

# colors
Ivory=hsv_to_rgb((47/360,0.06,1.00))
Red = hsv_to_rgb((14/360,1.00,0.85))
LightGreyGreen = hsv_to_rgb((150/360,0.24,0.66))
DarkerGreen = hsv_to_rgb((170/360,0.84,0.38))
DarkGreyBlue = hsv_to_rgb((193/360,0.87,0.21))

def f(x):
    return x**4-4.0, 4.0*x**3

def newton(func,x):
    f,fp = func(x)
    return x-f/fp



if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from matplotlib import rc
    
    # set up plot stzle
    plt.style.use('text-sans')
    rc('axes',titlesize='medium')
    
    r = np.sqrt(2.0)
    x0 = 2.0
    x = np.linspace(0.0,2.2,100)
    y,_ = f(x)
    y0,yp0 = f(x0)
    x1 = newton(f,x0)
    y1,_ = f(x1)
    fig = plt.figure(figsize=(2,2))
    ax = fig.add_subplot(111)
    ax.plot(x,y,color=DarkGreyBlue)
    ax.plot(x0,y0,color=DarkGreyBlue,marker='o')
    ax.vlines(x0,0.0,y0,linestyle=':',color=DarkGreyBlue)
    # ax.annotate(s=r'$f\,(x_0)$',xy=(x0,0.5*y0),xytext=(2,0),textcoords='offset points',\
    #     va='center',ha='left',size='small',color=DarkGreyBlue)
    # ax.annotate(s=r'$x_0$',xy=(x0,y0),\
    #     va='bottom',ha='right',xytext=(-4,4),textcoords='offset points',size='small',color=DarkGreyBlue)
    # ax.annotate(s=r'$x_1$',xy=(x1,y1),\
    #     va='bottom',ha='right',xytext=(-4,4),textcoords='offset points',size='small',color=Red)
    ax.plot([x0,x1],[y0,0.0],linestyle=':',color=Red)
    ax.plot(x1,y1,color=Red,marker='o')
    ax.vlines(np.sqrt(2.0),y.min(),y.max(),linestyle='-',linewidth=0.5,color=LightGreyGreen)
    ax.hlines(0,x.min(),x.max(),linestyle='-',linewidth=0.5,color=LightGreyGreen)
    ax.spines['left'].set_position(('outward',10))
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('outward',10))
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks([r,x1,x0])
    ax.xaxis.set_ticklabels([r'$r$',r'$x_1$',r'$x_0$'])
    ax.yaxis.set_ticks([0,y1,y0])
    ax.yaxis.set_ticklabels(['0',r'$f(x_1)$',r'$f(x_0)$'])
    
    fig.savefig('newton.pdf',format='pdf',bbox_inches='tight')
    