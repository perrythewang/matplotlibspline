from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

_num = 10

def plot_spline(x, y, fmt='-', kind='cubic', num=10, **kwargs):
    '''Equivalent to matplotlib.pyplot.plot except that spline interpolation
is used to smooth the curve. Only valid for 1 set of x and 1 set of y values.
    '''
    _num = num
    x = np.asarray(x).reshape(-1,1)
    y = np.asarray(y)
    x_intervals = np.concatenate([x[:-1], x[1:]], axis=1)

    # Split each interval into num parts
    x_smooth = np.apply_along_axis(_split_interval, axis=1, arr=x_intervals)
    x_smooth = np.append(x_smooth.flatten(), x[-1])

    # Interpolation
    func_smooth = interp1d(x.reshape(-1), y, kind=kind)
    y_smooth = func_smooth(x_smooth)

    return plt.plot(x_smooth, y_smooth, **kwargs)

def _split_interval(_slice):
    return np.linspace(_slice[0],
                       _slice[1],
                       num=_num,
                       endpoint=False)

# x = [0, 1, 2, 3, 5, 6, 7]
# y = [1, 1.4, 1.6, 1.7, 1.75, 1.775, 1.8]

# plot_spline(x, y, num=10, color='red')
# plt.show()
