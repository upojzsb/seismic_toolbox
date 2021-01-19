# Created by UPO-JZSB on Jan/17/2020
# Released Under GPL-v3.0 License

import numpy as np
import matplotlib.pyplot as plt


def wigb(a=None, scale=1, x=None, z=None, a_max=None, figsize=(30, 15), no_plot=False):
    """
    wigb - plot seismic trace data
    Thanks to XINGONG LI's contribution on MATLAB (https://geog.ku.edu/xingong-li)

    :param a: Seismic data (trace data * traces)
    :param scale: Scale factor (Default 1)
    :param x: x-axis info (traces) (Default None)
    :param z: z-axis info (trace data) (Default None)
    :param a_max: Magnitude of input data (Default None)
    :param figsize: Size of figure (Default (30, 15))
    :param no_plot: Do not plot immediately (Default False)
    :return: if no_plot is False, plot the seismic data, otherwise, do not plot immediately,
            users can adjust plot parameters outside
    """
    n_data, n_trace = a.shape

    if x is None:
        x = np.arange(n_trace)
    if z is None:
        z = np.arange(n_data)
    if a_max is None:
        a_max = np.mean(np.max(a, axis=0))

    x = np.array(x)
    z = np.array(z)

    dx = np.mean(x[1:]-x[:n_trace-1])
    dz = np.mean(z[1:]-z[:n_data-1])

    a *= scale*dx/a_max

    plt.figure(figsize=figsize)

    plt.xlim([-2*dx, x[-1] + 2*dx])
    plt.ylim([-dz, z[-1] + dz])
    plt.gca().invert_yaxis()

    for index_x in range(n_trace):
        trace = a[:, index_x]
        plt.plot(index_x*dx + trace, z, 'k-', linewidth=2)

        for (index_z, trace_val) in zip(range(n_data), trace):
            if trace_val <= 0:
                continue
            plt.plot([index_x*dx, index_x*dx+trace_val], [index_z*dz, index_z*dz], 'k-', linewidth=2)

    if not no_plot:
        plt.show()
