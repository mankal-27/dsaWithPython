from collections import Counter

arr = Counter([1,2,2,3,3,3,4,5,5])
print(arr)
print(arr[10])

print(arr.most_common(1))

print(list(arr.elements()))

arr.update([7,7,8])
print(list(arr.elements()))

arr.subtract([3,8,9])
print(list(arr.elements()))

c1 = Counter([1,3,3,2,2,2,4,4])
c2 = Counter([3,3,1,4,5])
c3 = c1 - c2
print(list(c3.elements()))