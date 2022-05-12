# 1,2,3,5,7 9 11,13, 15, 17
# 素数判定プログラム

for x in range(1, 101):
    flg = True
    if(x % 2 == 0):
        flg = False
    for y in range(2, x):
        if (x % y == 0):
            flg = False
    if (flg):
        print(x, "素数")
