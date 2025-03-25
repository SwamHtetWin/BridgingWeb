motorcycle = ['honda','yamaha','suzuki']
print(motorcycle)

motorcycle[0] = 'ducati'
print(motorcycle)

motorcycle.append('kawazaki')
print(motorcycle)

motorcycle.insert(0,'honda')
print(motorcycle)

car = []
car.append('BMW')
car.append('Mercedes')
car.append('Porshce')
print(car)

del motorcycle[0]
print(motorcycle)

popped_motorcycle = motorcycle.pop()        #pop = remove last item
print(f"reamining motorcycle after pop call {motorcycle}")
print(f"Popped motorcycle {popped_motorcycle}")

print(motorcycle)
print(f"popped element {motorcycle.pop(0)}")
print(f"remaining element {motorcycle}")