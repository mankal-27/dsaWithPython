def linearSearch(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False

print(linearSearch([2,3,4,5,6], 6))

print(7 in [9,4,5,6,7])
print("a" in "pythona")