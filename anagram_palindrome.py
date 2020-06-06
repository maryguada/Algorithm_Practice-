# given a string, return True or False if the word consist of an anagram in a palindrome

# hint : use dictionary to keep track of key and value pairs


def anagram_of_palindrome(word):
    a = {}
    for letter in word:
        # this is how we keep track of key & value pairs
        # take note of .get!! "a.get" the letter, and initiate the value to 0
        count = a.get(letter, 0)

        a[letter] = count + 1
        print(a)
    # we need to keep track of the odd count. If the odd count of two or more keys it greater than 1
    # then we know that it is not an anagram of a palindrome

    odd_count = 0
    # .values is a built in python fx.
    for count in a.values():
        if count % 2 != 0:  # if not even
            odd_count += 1

    if odd_count > 1:
        return False

    else:
        return True

    # test cases
x = 'aba'
y = 'aabc'  # {a:2 b:1 c:1}
z = 'racecar'  # {'r':2, 'a':2, c:2, e:1  }


print(anagram_of_palindrome(x))
# print(anagram_of_palindrome(y))
# print(anagram_of_palindrome(z))
