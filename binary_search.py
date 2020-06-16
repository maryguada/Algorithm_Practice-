# Write a function that takes in a sorted array of integers as well as a target integer. The function should use the
# binary search algorithm to determine if the target int is contained in the array and should return its index
# if it is otherwise -1.

# pseudocode:
# locate the left pointer at index[0], right pointer at the end of the array.
# create a helper function

# SOLUTION ONE : RECURSIVE

# O(log(n)) time | # O(log(n)) space


def binarySearch(array, target):
    return binaryHelper(array, target, 0, len(array)-1)


def binaryHelper(array, target, left, right):
    # base case first
    # is the left pointer, greater than the right pointer
    if left > right:
        return -1

    middle = (left + right) // 2  # this is rounding down the value in Python 3
    possible_match = array[middle]
    if target == possible_match:
        return middle
    elif target < possible_match:
        # we eliminate the RIGHT HALF of the array so we move right pointer -1
        return binaryHelper(array, target, left, middle-1)

    else:  # we eliminate the LEFT HALF of the array so we move left pointer +1
        if target > possible_match:
            return binaryHelper(array, target, middle+1, right)

# SOLUTION TWO: ITERATIVE

# O(log(n)) time | O(1) space


def binarySearch(array, target):
    return binaryHelper(array, target, 0, array(len)-1)


def binaryHelper(array, target, left, right):
    while left <= right:
        middle_pointer = (left+right) // 2
        possible_match = array[middle_pointer]
        if target == possible_match:
            return middle_pointer
        elif target < possible_match:
            right = middle_pointer - 1
        else:
            left = middle_pointer+1
    return -1
