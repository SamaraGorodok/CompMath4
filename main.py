import numpy as np
import matplotlib.pyplot as plt
from math import log, exp, sqrt

import plot
import qub
from exp import exp_func
from lin_func import lin_func
from log import log_func



from pow_aprox import pow_func
from sqrt import sqrt_func

IN = "input.txt"


def main():
    print("\nFILE - 1 \n KEYBOARD -2")
    choice = input()
    while (choice != '1') and (choice != '2'):
        print("\nFILE - 1 \n KEYBOARD -2")
        choice = input()

    if choice == '1':
        data = inp_file()
        if data is None:
            print("\nCant Read")
            data = inp()
    elif choice == '2':
        data = inp()

    answers = []
    temp_answers = [lin_func(data['dots']),
                    sqrt_func(data['dots']),
                    qub.qub_func(data['dots']),
                    exp_func(data['dots']),
                    log_func(data['dots']),
                    pow_func(data['dots'])]


    for answer in temp_answers:
        if answer is not None:
            answers.append(answer)

    print("\n\n%20s%20s" % ("Function", "Approx"))
    print("-" * 40)
    for answer in answers:
        if (answer is not None ):
            print("%20s%20.4f" % (answer['str_f'], answer['stdev']))
        else:
            print("Cant solve")
    x = np.array([dot[0] for dot in data['dots']])
    y = np.array([dot[1] for dot in data['dots']])
    plot_x = np.linspace(np.min(x), np.max(x), 100)
    plot_y = []
    labels = []
    for answer in answers:
        if (answer is not None ):
            plot_y.append([answer['f'](x) for x in plot_x])
            labels.append(answer['str_f'])
    plot.plot(x, y, plot_x, plot_y, labels)

    answw = min(answers, key=lambda x: x['stdev'])
    print("\nBest answer is :")
    print(answw['str_f'])

def inp_file():
    data = {'dots': []}

    with open(IN, 'rt', encoding='UTF-8') as fin:
        try:
            for line in fin:
                current_dot = tuple(map(float, line.strip().split()))
                if len(current_dot) != 2:
                    raise ValueError
                data['dots'].append(current_dot)
            if len(data['dots']) < 2:
                raise AttributeError
        except (ValueError, AttributeError):
            return None

    return data


def inp():
    data = {'dots': []}

    print("\nType coords \n type + to end ")
    while True:
        try:
            inp_data = input().strip()
            if inp_data == '+':
                if len(data['dots']) < 2:
                    raise ValueError
                break
            current_dot = tuple(map(float, inp_data.split()))
            if len(current_dot) != 2:
                raise ValueError
            data['dots'].append(current_dot)
        except ValueError:
            print("Type dot again")
    return data


main()
