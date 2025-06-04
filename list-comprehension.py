# List comprehensions

x = [i for i in range(10)]
print('Simple list comprehension: ', x)

x = [[j for j in range(5)] for i in range (10)]
print('Nested list comprehension: ', x)

x = [i for i in range(10) if i % 2 == 0]
print('List comprehension with if: ', x)