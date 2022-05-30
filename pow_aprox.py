import math
from math import *

import numpy as np

import acc_solver
import sys_solver

from lin_func import lin_func



def pow_func(dots):
    data = {}
    pts = []

    for i in dots:
        if i[0] <= 0:
            return None
        pts.append(i)
    n = len(dots)

    sx= 0
    for i in range(n):
        sx += pts[i][0]

    sx2 = 0
    for i in range(n):
        sx2 += pts[i][0] ** 2

    sy = 0
    for i in range(n):
        sy += math.log(pts[i][1])

    sxy = 0
    for i in range(n):
        sxy += pts[i][0] * math.log(pts[i][1])
    try:
        ans = sys_solver.calc([[sx2, sx, sxy], [sx, n, sy]], 2)
    except Exception:
        return None,None,None,None
    func = lambda x: np.exp(ans[1]) * np.exp(ans[0] * x)

    data['f'] = func

    data['str_f'] = f"fi = {round(math.exp(ans[1]),3)}*x^{round(ans[0],3)}"

    acc = acc_solver.acc(dots, func, n)
    data['s'] = acc

    data['stdev'] = acc_solver.mid(acc, n)
    return data
