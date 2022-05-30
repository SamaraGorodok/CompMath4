import math


def calc(array, n):
    max_iterations = 100000
    epsilon = 0.00001
    vector_old_ans = [0] * n
    vector_ans = [0] * n
    difference = epsilon + 1
    num = 0
    found_answer = True
    errors = [0] * n

    while difference > epsilon:
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += array[i][j] / array[i][i] * vector_ans[j]
            vector_ans[i] = array[i][n] / array[i][i] - sum
        for i in vector_ans:
            if i == None or i == math.inf or i == -math.inf:
                print("can't solve")
                found_answer = False
                exit(0)

        max_difference = 0.0
        for i in range(n):
            if abs(vector_old_ans[i] - vector_ans[i]) > max_difference:
                max_difference = abs(vector_old_ans[i] - vector_ans[i])
        difference = max_difference
        for i in range(n):
            vector_old_ans[i] = vector_ans[i]
        num += 1
        if (num >= max_iterations):
            print("can't solve")
            found_answer = False
            break
    return vector_ans
