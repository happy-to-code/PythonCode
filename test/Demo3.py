import copy

a = [1, 2, 3]
print(a)
b = [4, 5, 6]
print(b)
c = [a, b]
print(c)
e = copy.deepcopy(c)
print(e)
print("========================")
a.append(7)
print(a)
print(c[0])
print(e)
