from python_assignment.src.merge_the_tools.util import merge_the_tools

s = input()
k = int(input())
substrings = merge_the_tools(s,k)
for strings in substrings:
    print(strings)