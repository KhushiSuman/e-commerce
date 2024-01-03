max = int(input("Enter the max number"))

odd = []

for i in range(1, max):
    if i%2 == 1:
        odd.append(i)

print(odd)
""" max = int(input("Enter max number: "))

odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers) """