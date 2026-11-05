pin = "913"
n = 5

for i in range(10 ** n):
    if str(i).zfill(n) == pin:
        print(i)