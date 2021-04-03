import itertools

def mystery(word):
    return set("".join(perm) for perm in itertools.permutations(word))

x = len(mystery("ABBA"))
print(x)