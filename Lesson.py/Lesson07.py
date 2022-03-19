for i in range(5):
  print(i)

for i in range(5):
  if i == 3:
    break
  print(i)

for i in range(5):
  if i == 3:
    continue
  print(i)

for i in range(3):
  for j in range(3):
    print(i, j, sep="-")

arr = [2,4,6,8,10]

for i in arr:
  print(i)

arr = [2, 4, 6, 8, 10]
sum = 0
for w in arr:
  sum += w
  print(sum)