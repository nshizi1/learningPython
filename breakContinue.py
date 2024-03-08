for i in range(10):
    if i == 5:
        break
    print(i)
print("Loop stopped at 4")

for i in range(8):
    if i == 3:
        continue
    print(i)
print("loop skipped 3")