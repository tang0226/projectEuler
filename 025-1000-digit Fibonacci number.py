num1 = 0
num2 = 1
count = 1
while 1:
  count += 1
  store2 = num2
  num2 += num1
  num1 = store2
  if len(str(num2)) == 1000:
    break
  
print(count, len(str(num2)))
