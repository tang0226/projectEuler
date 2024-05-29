from time import time
start = time()
matrix = []
with open('Problem_data/Input_files/p107_network.txt') as f:
    line = f.readline().strip()
    while line:
        matrix.append(line.split(','))
        line = f.readline().strip()

numVertices = 40

edges = []

for y in range(numVertices - 1):
    for x in range(y + 1, numVertices):
        d = matrix[y][x]
        if d != '-':
            edges.append([int(d), (x, y)])
edges.sort()
saving = sum(list(i[0] for i in edges))
connected = list([i] for i in range(numVertices))

# Add smallest edges until all vertices are connected
for edge in edges:
    connect = edge[1]
    connect0 = connect[0]
    connect1 = connect[1]
    isConnected = connect0 in connected[connect1]
    if not isConnected:
        saving -= edge[0]
        new = list(i.copy() for i in connected)
        for add0 in connected[connect0]:
            new[add0] += connected[connect1]
        for add1 in connected[connect1]:
            new[add1] += connected[connect0]
        connected = new
    if len(connected[0]) == numVertices:
        break

print(saving)
print(str(time() - start) + ' s')