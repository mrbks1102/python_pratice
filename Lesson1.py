# 1-1 10進数から2進数にするプログラム

def dec2bin(target):
    amari = []

    # 割り算の商が０になるまで
    while target != 0:
        amari.append(target % 2)  # 余り
        target = target // 2  # 商

    amari.reverse()
    return amari
