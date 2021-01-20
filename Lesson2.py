def dec2bin_ex(target):
    # targetを整数部と少数部に分ける
    i = int(target)  # 整数部
    f = target - i  # 少数部

    # 整数部を2進数に変換
    a = []

    # 割り算の商が0になるまで
    while i != 0:
        a.append(i % 2)  # 余り
        i = i // 2       # 商

    # 要素を逆順にする
    a.reverse()

    # 少数部を2進数に変換
    b = []
    n = 0  # 繰り返した回数

    # 2を掛けた後の少数部が0になるまで
    while (f != 0):
        temp = f * 2  # 少数部×2
        b.append(int(temp))  # 整数部
        f = temp - int(temp)  # 少数部
        n += 1
        if (n >= 10):
            break

       # 2進数に変換した値
    return a, b
