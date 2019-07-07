import random

lst = [random.randint(-100, 100) for _ in range(10)]

print(lst)
lst2 = [item for item in lst if item % 3 == 0 and item > 0 and not item % 4 == 0 ]
print(lst2)
