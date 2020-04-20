import pyaudio
import wave,struct
import matplotlib.pyplot as plt
import threading
class PlotThread(threading.Thread):
    def __init__(self,  data):
        threading.Thread.__init__(self)
        self.data= data

    def run(self):
        while True:
            if self.data!=None:
                plot(self.data)


def plot(data):
    plt.ion()  # 开启interactive mode 成功的关键函数
    plt.figure(1)
    plt.plot(data, '-r')
    plt.show()
    plt.pause(0.02)
    plt.clf()  # 清除图像


class Recoder:
    p = pyaudio.PyAudio()
    types=pyaudio
    def init(self, callback, format, channels, rate, chunk, plot=True, plot_fps=25):
        if plot:
            self.count = 0
            self.plotThread=PlotThread(None)
            self.plotThread.start()
        stream = self.p.open(format=format,
                             channels=channels,
                             rate=rate,
                             input=True,
                             frames_per_buffer=chunk)
        format='>' +'h' * chunk
        while (True):
            data = struct.unpack(format, stream.read(chunk))

            callback(data)

            if plot :
                self.count+=1
                if self.count%((int((1 / plot_fps) * rate / chunk))+1)==0:
                    self.count=0
                    self.plotThread.data=data

if __name__=="__main__":
    def bla(data):
        pass


    CHUNK = 256
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 8000

    Recoder().init(callback=bla, format=FORMAT, channels=CHANNELS, rate=RATE, chunk=CHUNK)

