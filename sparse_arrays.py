# Complete the function matchingStrings in the editor below. The function must return an array of integers
# representing the frequency of occurrence of each query string in strings.


def matchingStrings(s, queries):
    return [s.count(q) for q in queries]


s = ['aba', 'baba', 'aba', 'xzxb']
queries = ['aba', 'xzxb', 'ab']

print(matchingStrings(s, queries))
