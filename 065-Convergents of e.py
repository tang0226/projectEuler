nums = [1, 2]
i = 1
j = 4
while len(nums) < 99:
    if i % 3 == 0:
        nums.append(j)
        j += 2
        i = 1
    else:
        nums.append(1)
        i += 1


currNum = 1
currDen = 1
for i in range(len(nums) - 2, -1, -1):
    currNum += currDen * nums[i]
    storeNum = currNum
    currNum = currDen
    currDen = storeNum
currNum += 2 * currDen


s = str(currNum)
total = 0
for i in range(len(s)):
    total += int(s[i])
print(total)
