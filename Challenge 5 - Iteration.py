list1 = ["cat", "dog", "bear"]

iterator = iter(list1)

for i in range(0, len(list1)):
    next_item = next(iterator)
    print(next_item)