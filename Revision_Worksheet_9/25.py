def ConvertOver(Num):
    Num.insert(0, Num[len(Num)-1])
    Num.pop()
    return Num

Num = [20, 30, 40, 50, 60, 70, 80, 90, 100, 10]
ConvertOver(Num)