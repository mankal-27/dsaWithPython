from collections import OrderedDict

od = OrderedDict([(1, "manju"), (3,"kalk"), (2,"belgaum")])

if 10 in od:
    print(od[10])
else:
    print("not in the dict")

od[10] = "messi"
print(od)

od.popitem()
print(od)