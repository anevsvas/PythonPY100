a = int(input("enter the number"))
b = int(input("enter the number"))
A_ = a ** 2
B_ = b ** 2
C_= A_ + B_
D_ = (a + b) ** 2
if  C_ > D_ :
    print(C_,  "сумма квадратов")
elif D_ > C_ :
    print(D_, "квадрат суммы")

else:
    print("суммы равны")