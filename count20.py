"""4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive"""

for val in range(1,21):
    print(val)

"""4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing CTRL-C or by closing the output window.)"""

millions = list(range(1,1001))
print(millions)
for number in millions:
    print(number, end=" ")