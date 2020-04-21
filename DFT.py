import numpy as np
import matplotlib.pyplot as plt


def dft(data,n=None):
    X=[]
    N=n
    if N==None:
        N=len(data)
    for k in range(N):
        XK=0
        for i in range(N):
            if i<len(data):
                XK+=data[i]*np.exp(np.complex(0,-1)*i*k*2*np.pi/N)
        X.append(XK)
    return np.array(X)

def idft(data,n=None):
    X=[]
    N=n
    if N==None:
        N=len(data)
    for k in range(N):
        XK=0
        for i in range(N):
            if i < len(data):
                XK+=data[i]*np.exp(np.complex(0,1)*i*k*2*np.pi/N)
        X.append(XK/N)
    return np.array(X)

if __name__=="__main__":
    X=np.array([1,2,3,4,5,6,7,8,9])
    Y=np.array([9,8,7,6,5,4,3,2,1])
    N=len(X)+len(Y)-1
    # The convolution of X and Y, N is the points the be calculated in dft process. To make the anwser complete, N must be greater than or equal to len(X)+len(Y)-1
    print(np.abs(idft(dft(X,N)*dft(Y,N),N)))
    print(np.abs(np.convolve(X,Y)))

