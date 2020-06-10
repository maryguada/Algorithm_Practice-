def validate(array, sequence):

    aIdx = 0
    seqIdx = 0

    while aIdx < len(array) and seqIdx < len(sequence):
        if array[aIdx] == sequence[seqIdx]:
            seqIdx += 1
        aIdx += 1

    if seqIdx == len(sequence):
        return True
    else:
        return False
    # return seqIdx == len(sequence)


a = [2, -7, 44, 31, -9, 10, -11]
b = [44, 31, -11]

c = [2, -7, 44, 31, -9, 10, -11]
d = [-12]

print(validate(a, b))
print(validate(c, d))
