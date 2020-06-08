
a_arr = [8, 5, 2, 9, 5, 6, 3]

# O(n^2) Time | O(1) Space

#=== SOLUTION 1 ===# 
#==================#

def insertSort(arr):
    for i in range(1, len(arr)):  # we want to start at index 1
        j = i
        # arr[j] is currently at 1 a& we compare it to arr[j-1] (THE NUMBER BEFORE J)
        while j > 0 and arr[j] < arr[j-1]:
            swap(j, j-1, arr)
            j -= 1
    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


print(insertSort(a_arr))

#=== SOLUTION 2 ===# 
#==================#


def insSort(arr):
    for i in range(1, len(arr)):
        j = i

        while j > 0 and arr[j] < arr[j-1]:
            swap(j, j-1, arr)
            j -= 1
    return arr
