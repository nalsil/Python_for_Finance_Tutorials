import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.dates import strpdate2num
import numpy as np

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

##run trading.py in iPython and call this method to see data plot
def graphRawFX():
    date,bid,ask = np.loadtxt('GBPUSD/GBPUSD1d.txt', unpack=True,
                              delimiter=',',
                              #converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})
                              converters={0:bytespdate2num('%Y%m%d%H%M%S')})

    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)

    ax1.plot(date, bid)
    ax1.plot(date, ask)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    plt.grid(True)
    plt.show()

graphRawFX()
