# wigb tester
import matplotlib.pyplot as plt
import scipy.io
import visualization.wigb


data = scipy.io.loadmat('./concentric_trace.mat')['gongzhongxindiandaoji']
visualization.wigb.wigb(
    a=data,
    x=[60*i for i in range(60)],
    z=[0.001*i for i in range(data.shape[0])],
    no_plot=True,
    direction='Vertical'
)

plt.xlabel('Offset/m')
plt.ylabel('Time/s')
plt.title('Concentric Trace Record (Before Correction)')

plt.show()

visualization.wigb.wigb(
    a=data,
    x=[60*i for i in range(60)],
    z=[0.001*i for i in range(data.shape[0])],
    no_plot=True,
    direction='Horizontal'
)

plt.ylabel('Offset/m')
plt.xlabel('Time/s')
plt.title('Concentric Trace Record (Before Correction)')

plt.show()
