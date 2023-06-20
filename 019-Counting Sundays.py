import time
start = time.time()
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayNum = 1
dayWeek = 0
dayMonth = 1
amount = 368
month = 0
year = 1901
total = 0
#year > 2000
while year <= 2000:
  dayWeek = dayNum % 7
  if dayMonth > months[month]:
    dayMonth = 1
    month += 1
  if month > 11:
    month = 0
    year += 1
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        months[1] = 29
      else:
        months[1] = 28
    else:
      months[1] = 28
  else:
    months[1] = 28
  if dayMonth == 1 and dayWeek == 0 and year > 190:
    total += 1
  dayMonth += 1
  dayNum += 1
print(total)
end = time.time() - start
print("time taken: " + str(end) + " sec")