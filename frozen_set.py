set1 = frozenset([1,2,3,4,5,6])
set2 = frozenset([4,5,6,7,8,9])

#frozen sets

union = set1.union(set2)
print(union)

intersection= set1.intersection(set2)
print(intersection)

difference = set1 - set2
print(difference)

symdiff = set1 ^ set2
print(symdiff)

