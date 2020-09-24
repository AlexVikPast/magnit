# Выборка по максимальному значению из словаря
dc = {}
dc = {'Мясо': 5, 'Молоко': 5, 'Сыр': 2, 'Хлеб': 3}

print(dc)


def min_max_dc(dc, min_max):

    if min_max == 'min':
        val = min(dc.values())
    elif min_max == 'max':
        val = max(dc.values())
    return {k: v for k, v in dc.items() if v == val}


print(min_max_dc(dc, 'max'))
print(min_max_dc(dc, 'min'))