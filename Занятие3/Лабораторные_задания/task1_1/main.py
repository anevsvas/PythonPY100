def task_1():
    max_sum = 500
    current_sum = 0
    n = 1
    while True :
        current_value = n ** 2
        current_sum += n ** 2

        if current_sum > max_sum :
            break
            return n
        else:
            print(n, current_sum)
            n = n + 1








if __name__ == "__main__":
    print (task_1())



