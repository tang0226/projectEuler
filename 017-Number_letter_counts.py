import time
start = time.time()
ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
teens = [0, 6, 6, 8, 8, 7, 7, 9, 8, 8]
hundreds = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
total = 0
for i in range(1, 1001):
  num = i
  text = str(i)
  added = total;
  if len(text) == 1:
    total += ones[int(text[0])]
  elif len(text) == 2:
    if num > 10 and num < 20:
      total += teens[int(text[1])]
    else:
      total += tens[int(text[0])]
      total += ones[int(text[1])]
  elif len(text) == 3:
    if text[1] == "0" and text[2] == "0":
      total += hundreds[int(text[0])] + 7
    else:
      total += hundreds[int(text[0])] + 10
    if int(text[1:3]) > 10 and int(text[1:3]) < 20:
      total += teens[int(text[2])]
    else:
      total += tens[int(text[1])]
      total += ones[int(text[2])]
  else:
    total += 11
print(total)
end = time.time() - start
print("time taken: " + str(end) + " sec")