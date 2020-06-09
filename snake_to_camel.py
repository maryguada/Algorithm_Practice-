# Given a variable name in snake_case, return variable name to camelCase
def snake_to_Camel(var_name):
    # In snake_case, we typically see "_"
    # .split will separate the words inbetween "_"
    words = var_name.split("_")
    # print(words)

    # we start at index 1 and skip 0 index because we want to capitalize words after index 0.
    for i in range(1, len(words)):
        # print(words[i])
        words[i] = words[i].capitalize()
    return "".join(words)


a = 'hello_world'
b = 'monty_python_world'

print(snake_to_Camel(a))
print(snake_to_Camel(b))
