import sys
import math

arr = [1,5,6,9,5,4]
print(sorted(arr))
print(arr)

fruits_list = ["apple", "kiwi", "chickooo"]
print(max(fruits_list, key=len))

print(sum(arr, start=10))
print(math.prod(arr))

arr1 = [True, False, True]
print(any(arr1))
print(all(arr1))

def count_element_in_list(arr, number):
    cnt = 0
    for ele in arr:
        if ele == number:
            cnt = cnt + 1
    return cnt

print(arr.count(5))
print(count_element_in_list(arr, 5))

arr2 = [5,6,2,4]  #[index, value] (0,5),(1,6),(2,2),(3,4)
print(list(enumerate(arr2)))

for i, val in list(enumerate(arr2)):
    print(i, val)

arr3 = [5,6,4]
print(list(reversed(arr3)))

arr4 = list(range(5))
print(arr4)