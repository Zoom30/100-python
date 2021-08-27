# In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

# Examples:

# permutations('a'); # ['a']
# permutations('ab'); # ['ab', 'ba']
# permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
from itertools import permutations as pm
def permutation(string):
    letter_list = []
    for letter in string:
        letter_list.append(letter)

    perm_list = []
    perm = pm(letter_list)
    for i in perm:
        perm_list.append("".join(i))
    return perm_list



print(permutation("aabb"))