import matplotlib
%matplotlib inline
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np

def plot_grid(X,d1,d2,title0='',order='C'):
    #takes a NxD matrix and plots N d1xd2 images (where d1xd2==D)
    (N,D) = np.shape(X)
    assert d1*d2==D,'%i %i %i'%(d1,d2,D)
    n1 = int(np.sqrt(N))+1
    for n in range(0,N):
        #pl = subplot(n1,n1,n)
        plt.figure()
        x = np.reshape(X[n,:],(d1,d2),order=order)
        imgplot = plt.imshow(x, cmap=cm.Greys_r) #, vmin=0, vmax=2)
        imgplot.set_interpolation('nearest')