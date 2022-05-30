

import acc_solver
import sys_solver


def sqrt_func(dots):
    data = {}
    n = len(dots)
    n = len(dots)
    x = [i[0] for i in dots]
    y = [j[1] for j in dots]

    sx = sum(x)
    sx2 = sum([xi ** 2 for xi in x])
    sx3 = sum([xi ** 3 for xi in x])
    sx4 = sum([xi ** 4 for xi in x])
    sy = sum(y)
    sxy = sum([x[i] * y[i] for i in range(n)])
    sx2y = sum([(x[i] ** 2) * y[i] for i in range(n)])

    system = [
        [n, sx, sx2, sy],
        [sx, sx2, sx3, sxy],
        [sx2, sx3, sx4, sx2y]
    ]
    ans = sys_solver.calc(system,3)
    f = lambda x: ans[2] * (x ** 2) + ans[1]*x + ans[0]
    data['f'] = f

    data['str_f'] = f"fi = {round(ans[2],3)}*x^2 + {round(ans[1],3)}*x + {round(ans[0],3)}"

    acc = acc_solver.acc(dots, f, n)
    data['s'] = acc

    data['stdev'] = acc_solver.mid(acc, n)


    return data

