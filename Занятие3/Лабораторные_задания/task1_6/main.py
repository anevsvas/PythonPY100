def money(a , b, add, m):
    gen_a = a * m  # кол-во поступлений
    gen_b = 0


    for i in range (m):
        gen_b = gen_b + b
        b= b * (1 + add)
    return gen_b - gen_a

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = 10

    add = 0.03
    print(money(a, b, add, m))

