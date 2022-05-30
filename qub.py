import acc_solver
import sys_solver
import numpy
def qub_func(dots):
    data = {}
    n = len(dots)
    n = len(dots)
    x = [i[0] for i in dots]
    y = [j[1] for j in dots]

    sx = sum(x)
    sx2 = sum([xi ** 2 for xi in x])
    sx3 = sum([xi ** 3 for xi in x])
    sx4 = sum([xi ** 4 for xi in x])
    sx5 = sum([xi ** 5 for xi in x])
    sx6 = sum([xi ** 6 for xi in x])
    sy = sum(y)
    sxy = sum([x[i] * y[i] for i in range(n)])
    sx2y = sum([(x[i] ** 2) * y[i] for i in range(n)])
    sx3y = sum([(x[i] ** 3) * y[i] for i in range(n)])

    system = [
        [n,sx,sx2,sx3,sy],
        [sx,sx2,sx3,sx4,sxy],
        [sx2,sx3,sx4,sx5,sx2y],
        [sx3,sx4,sx5,sx6,sx3y]
    ]
    ans = sys_solver.calc(system,4)

    res_func = lambda x: ans[3]*(x**3)+ans[2]*(x**2)+ans[1]*x+ans[0]
    data['f'] = res_func

    data['str_f'] = f"fi = {round(ans[3], 3)}*x^3 + {round(ans[2], 3)}*x^2 + {round(ans[1], 3)}x + {round(ans[0], 3)}"

    acc = acc_solver.acc(dots, res_func, n)
    data['s'] = acc
    print("\n")
    for i in range(len(x)):
        print(x[i],y[i],round(res_func(x[i]),3),round(acc[i],3))


    data['stdev'] = acc_solver.mid(acc, n)

    return data