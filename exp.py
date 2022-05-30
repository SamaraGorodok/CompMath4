import math

import numpy as np

import acc_solver
import sys_solver



from math import *


def exp_func(dots):
    data = {}


    pts = []
    for i in dots:
        if i[0] == 0:
            pts.append([i[0] + 0.001], i[1] + 0.001)
        else:
            pts.append(i)

    n = len(pts)

    # print(pts)

    sx = 0
    for i in range(n):
        sx += pts[i][0]

    summ_x_sqd = 0
    for i in range(n):
        summ_x_sqd += pts[i][0] ** 2

    summ_y = 0
    for i in range(n):
        summ_y += math.log(pts[i][1])

    summ_x_y = 0
    for i in range(n):
        summ_x_y += pts[i][0] * math.log(pts[i][1])
    try:
        ans = sys_solver.calc([[summ_x_sqd, sx, summ_x_y], [sx, n, summ_y]], 2)
    except Exception:
        ans = 0
    result_func = lambda x: np.exp(ans[1]) * np.exp(ans[0] * x)

    data['str_f'] = f"fi = {round(math.exp(ans[1]),3)}*e^{round(ans[0], 3)}"
    data['f'] = result_func

    acc = acc_solver.acc(dots, result_func, n)
    data['s'] = acc

    data['stdev'] = acc_solver.mid(acc, n)

    return data
