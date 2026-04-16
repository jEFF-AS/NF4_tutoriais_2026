import sys
from itertools import permutations

letters = sys.argv[1]

words = set()

# gera palavras simples (didático)
for i in range(1, len(letters)+1):
    for p in permutations(letters, i):
        words.add("".join(p))

# imprime cada palavra em uma linha (igual C++)
for w in sorted(words):
    print(w)
