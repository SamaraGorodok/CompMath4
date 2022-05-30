import math

import numpy as np

import acc_solver
import sys_solver

from lin_func import lin_func
from  math import *



def log_func(dots):
    data = {}

    pts = []
    length = len(dots)

    for i in dots:
        if i[0] == 0:
            pts.append([i[0] + 0.001], i[1] +0.001)
        else:
            pts.append(i)
    length = len(pts)
    sx = 0

    for i in range(length):
        sx += math.log(pts[i][0])

    sx2 = 0
    for i in range(length):
        sx2 += math.log(pts[i][0]) ** 2

    sy = 0
    for i in range(length):
        sy += pts[i][1]

    sxy = 0
    for i in range(length):
        sxy += math.log(pts[i][0]) * pts[i][1]

    # try:

    ans = sys_solver.calc([[sx2, sx, sxy], [sx, length, sy]], 2)
    if ans == 0:
        ans += 0.0001
    # except Exception:
    #     return None
    func = lambda x: ans[0] * np.log(x) + ans[1]

    data['f'] = func
    data['str_f'] = f"fi = {round(ans[0],3)}*ln(x) + {round(ans[1],3)}"

    acc = acc_solver.acc(pts, func, length)
    data['s'] = acc

    if (length == 0):

        length += 0.001
    data['stdev'] = acc_solver.mid(acc, length)

    return data
