import math

import acc_solver
import sys_solver





def lin_func(dots):
    data = {}

    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]

    sx = sum(x)
    sx2 = sum([xi ** 2 for xi in x])
    sy = sum(y)
    sxy = sum([x[i] * y[i] for i in range(n)])

    mid_x = sx/n
    mid_y = sy/n

    chisl = 0
    for i in range(n):
        chisl += (dots[i][0] - mid_x) * (dots[i][1] - mid_y)
    znam2 = 0
    for i in range(n):
        znam2 += (dots[i][0] - mid_x)**2
    znam3 = 0
    for i in range(n):
        znam3 += (dots[i][1]- mid_y)**2
    try:
        r = (chisl)/(math.sqrt(znam2*znam3))
        print ("coef")
        print(r)
    except Exception:
        print("Cant solve coef")
    ans = sys_solver.calc([[sx2, sx, sxy], [sx, n, sy]], 2)
    func = lambda x: ans[0]*x+ans[1]

    data['f'] = func

    data['str_f'] = f"fi = {round(ans[0],3)}x + {round(ans[1],3)}"

    acc = acc_solver.acc(dots,func,n)
    data['s'] = acc

    data['stdev'] = acc_solver.mid(acc,n)

    return data
