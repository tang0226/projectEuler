triangle = 1
pentagon = 1
hexagon = 1
triangles = [1]
pentagons = [1]
hexagons = [1]
triangleChange = 2
pentagonChange = 4
hexagonChange = 5
for i in range(0, 287):
	triangle += triangleChange
	triangleChange += 1
	triangles.append(triangle)

	pentagon += pentagonChange
	pentagonChange += 3
	pentagons.append(pentagon)

	hexagon += hexagonChange
	hexagonChange += 4
	hexagons.append(hexagon)

i = 285
done = False
while not(done):
	i += 1
	triangle += triangleChange
	triangleChange += 1
	triangles.append(triangle)

	pentagon += pentagonChange
	pentagonChange += 3
	pentagons.append(pentagon)

	hexagon += hexagonChange
	hexagonChange += 4
	hexagons.append(hexagon)

	if pentagons.count(triangles[i]) == 1 and hexagons.count(triangles[i]) == 1:
		done = True
print(triangles[i])