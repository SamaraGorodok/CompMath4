import math


def acc(dots,func,length):
    accuracy = [(dots[i][1] - func(dots[i][0])) ** 2 for i in range(length)]
    return accuracy

def mid(acc,length):
    mid_acc = math.sqrt(sum(acc)/length)
    return mid_acc