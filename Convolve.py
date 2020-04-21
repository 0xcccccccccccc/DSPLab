import numpy as np
import DFT

def circularConvolve(x, y, n):
    '''
    y_c(n)=\sum_{m=0}^{N-1}x(m)h((n-m)%N)
    '''
    Y=[]
    for k in range(n):
        sum = 0
        for i in range(n):
            if i < len(y) and (k - i)%n<len(x):
                sum += y[i] * x[(k - i)%n]
        Y.append(sum)
    return np.array(Y)


def circularConvolve2(x, y, n):
    return DFT.idft(DFT.dft(x, n) * DFT.dft(y, n), n)

def linearConvolve(x,y):
    return np.convolve(x,y)

def linearConvolve2(x,y):
    n=len(x)+len(y)-1
    return DFT.idft(DFT.dft(x, n) * DFT.dft(y, n), n)

def linearConvolve3(x:np.array,y:np.array,points_per_part:int):
    '''
    overlap add method
    '''
    __temp=[x,y] if len(x)>len(y) else [y,x]
    X=__temp[0] # the longer series
    H=__temp[1] # the shorter series
    M = len(X) # length of the longer series
    N = len(H) # length of the longer series

    # now we are going to split the X into segments
    X=np.concatenate([X,np.zeros(points_per_part-M%points_per_part)]) # add zeros to make the last segment consistent with the length of other segmentss
    parts=np.hsplit(X,range(points_per_part,M,points_per_part)) # now split it

    # array to store the result
    result=np.array([])

    for part in parts:
        '''
        For each piece of data, do L point circular convolution with H, keeping the last M-1 points
        '''
        L=points_per_part+N-1
        conv=circularConvolve(part,H,L)
        result=np.concatenate([result,conv[L-M:]])

    return result




if __name__=="__main__":
    X = np.array([1, 2, 3, 4, 5,6,7,8,9,1,2,3,4,5,6,76])
    Y = np.array([6, 7, 8, 9])
    N = len(X) + len(Y) - 1
    print(abs(circularConvolve2(Y, X, N)))
    print(abs(circularConvolve(Y, X, N)))
    print(linearConvolve3(X,Y,5))
