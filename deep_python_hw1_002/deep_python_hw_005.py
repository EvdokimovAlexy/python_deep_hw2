# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
import collections
from itertools import count

my_list = [2, 5, 2, 8, 9, 6, 8, 1, 10]
result_list = []
print(my_list)
print([i for i,  count in collections.Counter(my_list).items() if count > 1])
[result_list.append(x) for x in my_list if x not in result_list]

print(result_list)
