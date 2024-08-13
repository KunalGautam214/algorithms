import random


def sort_list_by_sort_key(a):
    # create sort key to sort a list
    p = random.sample(range(1, 100), 4)
    print('List to sort', a)
    print('Sort key', p)
    d = {}
    # map list with sort key here I used dictionary to map list with sort key
    for i, j in zip(a, p):
        d[j] = i
    # sort dictionary on sort key
    sorted_dict = dict(sorted(d.items(), key=lambda x: x[0]))
    return list(sorted_dict.values())


a_1 = [1, 2, 3, 4]
p = [36, 3, 62, 19]
b = [2, 4, 1, 3]
sorted_a = sort_list_by_sort_key(a_1)
print(sorted_a)
