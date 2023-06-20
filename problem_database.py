import datetime
import os

# Array functions:
def heapify(arr, n, i, func):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2
	if l < n and func(arr[l]) > func(arr[largest]):
		largest = l
	if r < n and func(arr[r]) > func(arr[largest]):
		largest = r
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest, func)
def heapSort(arr, func):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, func)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, func)

# Date functions
# Days per year: ~365.25
# Days per month: ~365.25/12
# Hours per day: 24
# Minutes per day: 1440
# Seconds per day: 86400
def format(date):
	return date.strftime("%d %B %Y %I%p")

def toDelta(seconds):
	return datetime.timedelta(seconds=seconds)

def toSeconds(delta):
	return delta.days * 86400 + delta.seconds

def toMinutes(delta):
	return toSeconds(delta) / 60

def toHours(delta):
	return toMinutes(delta) / 60

def toDays(delta):
	return toHours(delta) / 24

def toWeeks(delta):
	return toDays(delta) / 7

def toMonths(delta):
	return toDays(delta) * 12 / 365.25

def toYears(delta):
	return toMonths(delta) / 12


# Get the starting point date
published1 = 1002301200
date1 = datetime.datetime(2001, 10, 5, 10, 0, 0)
start = date1 - toDelta(published1)

# Problem class
class Problem:
	def __init__(self, id, description, published, solvedBy, solveStatus, currTime):
		self.id = id
		self.description = description
		self.published = start + toDelta(int(published))
		self.solvedBy = int(solvedBy)
		self.solveStatus = solveStatus

		timeSincePublished = currTime - self.published
		self.solvesPerYear = self.solvedBy / toYears(timeSincePublished)
		self.solvesPerMonth = self.solvedBy / toMonths(timeSincePublished)
		self.solvesPerWeek = self.solvedBy / toWeeks(timeSincePublished)
		self.solvesPerDay = self.solvedBy / toDays(timeSincePublished)
		self.solvesPerHour = self.solvedBy / toHours(timeSincePublished)
		self.solvesPerMinute = self.solvedBy / toMinutes(timeSincePublished)
		self.solvesPerSecond = self.solvedBy / toSeconds(timeSincePublished)

# Uh, default timezone is 7 hrs ahead?
now = datetime.datetime.now() - datetime.timedelta(seconds=7*3600)
		
# Initialize list of problems
problems = []
with open("./prob_data.txt") as fp:
	line = fp.readline()
	line = fp.readline().strip()
	while line:
		data = line.split("##")
		problems.append(Problem(data[0], data[1], data[2], data[3], data[4], now))
		line = fp.readline().strip()

"""param = "hour"
heapSort(problems, lambda x: x.solveRate(param, now))
problems.reverse()
for i in problems:
	print("#" + i.id, i.description, round(i.solveRate(param, now), 6))"""
"""
+--------+
|My Text |
+--------+
|Hey     |
+--------+--
"""
def drawTable(data, attr, col):
	maxWidths = []
	for i in range(len(col)):
		maxWidths.append(max(list(len(str(getattr(j, attr[i]))) for j in data) + [len(col[i])]))
	
	divider = "+"
	for i in maxWidths:
		divider += "-" * (i + 2) + "+"
	print(divider)
	
	print("|", end="")
	for i in range(len(col)):
		print(" " + col[i] + (" " * (maxWidths[i] - len(col[i]))) + " |", end="")
	print()
	
	print(divider)

	for line in data:
		print("|", end="")
		for i in range(len(col)):
			d = str(getattr(line, attr[i]))
			print(" " + d + (" " * (maxWidths[i] - len(d))) + " |", end="")
		print()

	print(divider)
	#return divider

attributes = ["id", "description", "solvesPerDay"]
sortBy = "solvesPerDay"
heapSort(problems, lambda p: getattr(p, sortBy))
problems.reverse()
drawTable(problems[ : 400], attributes, attributes)