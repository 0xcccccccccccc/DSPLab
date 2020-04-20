
import pyaudio
import wave,struct
import matplotlib.pyplot as plt
import threading
class PlotThread(threading.Thread):
    '''
    The wave plotting thread.
    '''
    def __init__(self,  data):
        threading.Thread.__init__(self)
        self.data= data

    def run(self):
        while True:
            if self.data!=None:
                plot(self.data)


def plot(data):
    plt.ion()  # interactive mode
    plt.autoscale(enable=False)
    plt.xlim(0,len(data))
    plt.ylim(-32767,32767)
    plt.figure(1)
    plt.plot(data, '-r')
    plt.show()
    plt.pause(0.02)
    plt.clf()


class Recoder:
    __p = pyaudio.PyAudio()
    types=pyaudio
    def init(self, callback, format, channels, rate, chunk, plot=True, plot_fps=25):

        '''
        Once an instance of a Recorder was initiated it will call the callback function continually. Note that callback function may block the whole process.
        :param callback: The funtion to be called when a new batch of aduio data received
        :param format: Sample Depth
        :param channels: Dual/Mono channel
        :param rate: Sample rate
        :param chunk: The size of each batch
        :param plot: Enable the wave plotting
        :param plot_fps: How many frames will be refreshed when plotting waves.
        :return:None
        '''
        if plot:
            self.count = 0
            self.plotThread=PlotThread(None)
            self.plotThread.start()
        stream = self.__p.open(format=format,
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

