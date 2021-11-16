# Created by UPO-JZSB on Jan/17/2021
# Released Under GPL-v3.0 License

# Version 0.1 is released on Jan/17/2021
# Implementation of wigb

# Version 0.2 is released on Jan/19/2021
# Add parameter direction - decide the plot direction

# Version 0.3 is released on Jan/20/2021
# Replace `plot' by `fill_between' function to boost the filling procession

# Version 0.4 is released on Nov/16/2021
# Fixed a problem which may cause inconsistent display
# Fixed a problem which may change original data

import numpy as np
import copy
import matplotlib.pyplot as plt


def wigb(a=None, scale=1, x=None, z=None, a_max=None, figsize=(30, 15), no_plot=False, direction='Vertical'):
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
    :param direction: Display direction (Default 'Vertical'). Either 'Vertical' or 'Horizontal'

    :return: if no_plot is False, plot the seismic data, otherwise, do not plot immediately,
            users can adjust plot parameters outside
    """
    a = copy.copy(a)
    n_data, n_trace = a.shape

    if x is None:
        x = np.arange(n_trace)
    if z is None:
        z = np.arange(n_data)
    if a_max is None:
        a_max = np.max(np.max(a, axis=0))
    if direction not in ['Horizontal', 'Vertical']:
        raise ValueError('Direction must be \'Horizontal\' or \'Vertical\'')

    x = np.array(x)
    z = np.array(z)

    dx = np.mean(x[1:] - x[:n_trace - 1])
    dz = np.mean(z[1:] - z[:n_data - 1])

    a *= scale * dx / a_max

    plt.figure(figsize=figsize)

    if direction == 'Vertical':
        plt.xlim([-2 * dx, x[-1] + 2 * dx])
        plt.ylim([-dz, z[-1] + dz])
        plt.gca().invert_yaxis()

        for index_x in range(n_trace):
            zero_offset = index_x*dx
            trace = a[:, index_x]
            plt.plot(zero_offset + trace, z, 'k-', linewidth=2)
            plt.fill_betweenx(
                np.array([y * dz for y in range(n_data)]),
                np.zeros_like(np.arange(n_data)) + zero_offset,
                trace + zero_offset,
                where=trace > 0,
                interpolate=True,
                color='k',
                antialiased=True
            )

    elif direction == 'Horizontal':
        plt.xlim([-dz, z[-1] + dz])
        plt.ylim([-2 * dx, x[-1] + 2 * dx])
        plt.gca().invert_yaxis()

        for index_z in range(n_trace):
            zero_offset = index_z*dx
            trace = a[:, index_z]
            plt.plot(z, zero_offset + trace, 'k-', linewidth=2)

            plt.fill_between(
                np.array([y * dz for y in range(n_data)]),
                np.zeros_like(np.arange(n_data)) + zero_offset,
                trace + zero_offset,
                where=trace > 0,
                interpolate=True,
                color='k',
                antialiased=True
            )

    if not no_plot:
        plt.show()
