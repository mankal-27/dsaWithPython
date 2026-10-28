import time

startTime = time.time()

for i in range(1, 6):
    print(i)

endTime = time.time()

finalTime = endTime - startTime
print(finalTime)