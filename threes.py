threes = list(range(3,31,3))
for three in threes:
    print(three)

cubes = []
for value in range(1,11):
    cubes.append(value**3)
print("First Ten Cubes")
print(cubes)
print("\n")

cube_list = [value ** 3 for value in range(1,11)]
print(cube_list)