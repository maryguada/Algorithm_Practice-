def stairs(n):
    for i in range(1, n+1):
        # print(i, n+1)
        print(str('#'*i).rjust(n))


a = 5
b = 10
print(stairs(a))
print(stairs(b))

# ==========
# SOLUTION 2
# ==========


def staircase(n):
    print_sc = ''
    for i in range(1, n+1):
        if (i < n):
            print_sc += ' '*(n-i) + '#'*(i) + '\n'
        else:
            print_sc += '#'*1
    print(print_sc)


# print(staircase(a))
# print(staircase(b))
