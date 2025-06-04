''' 
Immutable types:
str
int
float
bool
bytes
tuple

Mutable types:
list
set
dict
(third party types)
'''

# Immutable tuple
x = (1, 2)
y = x

x = (1, 2, 3)

print('Immutable tuple: ', x, y, '(y is a reassignable copy of x)')


# Mutable list
x = [1, 2]
y = x

x[0] = 100

print('Mutable list: ', x, y, '(y is a refernce to x)')


# Get largest numbers

def get_largest_numbers(numbers, n):
    numbers.sort() # This will sort the list in place (side effect)

    return numbers[-n:] # counting from end of list, go n back

nums = [2, 3, 4, 1, 34, 123, 321, 1]
print('Unsorted list: ', nums)

largest = get_largest_numbers(nums, 2) # Variable assign not strictly necessary
print('Sorted list: ', nums)


