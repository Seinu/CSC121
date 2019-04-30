from random import randint
set1 = set()
set2 = set()
for i in range(0, 5):
    set1.add(randint(1, 10))
    set2.add(randint(1, 10))

print("set1: ", set1)
print("set2: ", set2)
print("Union of set1 and set2: ", set1.union(set2))
print("Odd numbers in union of set1 and set2: ", {
      x for x in set1.union(set2) if x % 2 == 1})
print("Intersection of set1 and set2: ", set1 & set2)
print("Symmetric difference of set1 and set2: ", set1 ^ set2)
