numbers = [54, 5, 2456, 11, 95]

smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n

print(min(numbers))