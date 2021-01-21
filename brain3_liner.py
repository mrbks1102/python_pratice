# -*- coding: utf-8 -*-
def linear_search(data, value):
    for i in range(len(data)):
        if data[i] == value:  # 欲しい値が見つかったら
            return i
    return -1  # 欲しい値が見つからなかったら


data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
print(linear_search(data, 40))

# このような単純な処理にpythonはindexという関数を用意しています
data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
print(data.index(40))
