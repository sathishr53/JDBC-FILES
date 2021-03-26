from collections import Counter
a = [1, 1, 2, 3, 2, 2, 4, 5, 4, 5, 4, 3, 6, 2, 2]
C = Counter (a)
print (C)
print (list(C.elements()))
print (C.most_common ())
sub = {2: 1, 6: 1}
print (C.subtract (sub))
print (C.most_common())