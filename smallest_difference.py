# Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose
# absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

# You can assume that there will only be one pair of numbers withe the smallest difference.

# Pseudocode:
# sort the array, that is a more efficient way to find the smallest difference.

# O(nlog(n) time) | O(1) space


def smallest_diff(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    idxOne = 0
    idxTwo = 0

    result_smallest = float("inf")
    current_dif = float("inf")
    paired_diff = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        left_num = arrayOne[idxOne]
        right_num = arrayTwo[idxTwo]
        # if left array less than right array, increment left array pointer / idxOne
        if left_num < right_num:
            current_dif = right_num - left_num
            idxOne += 1
        # if right array less than left array, increment right array pointer / idxTwo
        elif right_num < left_num:
            current_dif = left_num - right_num
            idxTwo += 1
        else:  # if both numbers equal to zero.
            return [left_num, right_num], "is equal to zero"

        if result_smallest > current_dif:
            result_smallest = current_dif
    return paired_diff
