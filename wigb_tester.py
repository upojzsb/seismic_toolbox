# wigb tester
import matplotlib.pyplot as plt
import scipy.io
import visualization.wigb


data = scipy.io.loadmat('./concentric_trace.mat')['gongzhongxindiandaoji']


visualization.wigb.wigb(
    a=data,
    x=[60*i for i in range(60)],
    z=[0.001*i for i in range(data.shape[0])],
    no_plot=True
)

plt.xlabel('Offset/m')
plt.ylabel('Time/s')
plt.title('Concentric Trace Record (Before Correction)')

plt.show()
