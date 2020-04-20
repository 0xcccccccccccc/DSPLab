from IO import Recorder
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 205
FORMAT = Recorder.Recoder.types.paInt16
CHANNELS = 1
RATE = 8000
JUNCTION=1.4*10**11

TABLE=[
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]

R=RATE
N=CHUNK
f=np.array([697,770,852,941,1209,1336,1477,1633])
K=np.rint(N*f/R)
w = 2*np.pi*K / N
C = 2*np.cos(w)

def plot(data):
    plt.ion()  # 开启interactive mode 成功的关键函数
    plt.autoscale(enable=False)
    plt.xlim(0,8)
    plt.ylim(0,20)
    plt.stem(data)
    plt.show()
    plt.pause(0.002)
    plt.clf()  # 清除图像

def recongnize(data):
    q1 = np.zeros(8)
    q2 = np.zeros(8)
    for i in data:
        q0=C*q1-q2+i
        q2=q1
        q1=q0
    p=np.power(q1,2)+np.power(q2,2)-C*q1*q2-9*10**10
    #pdb=np.log10(p)-10
    #plot(pdb)
    px=np.max(p[0:4])
    py=np.max(p[4:8])
    if px>JUNCTION and py>JUNCTION:
        ipx=p[0:4].argmax()
        ipy=p[4:8].argmax()
        print(TABLE[ipx][ipy])



recorder= Recorder.Recoder()
recorder.init(callback=recongnize,format=FORMAT, channels=CHANNELS, rate=RATE, chunk=CHUNK,plot=False)
