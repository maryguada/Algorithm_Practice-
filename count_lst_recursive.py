# Return the number of items in a list, using recursion
# Recursive means when a function calls on itself.


def count_recursively(lst):
    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])


a = [0, 0, 0, 1, 1]
z = [0, 1, 1]
y = 'str'

print(count_recursively(a))
print(count_recursively(z))
print(count_recursively(y))
