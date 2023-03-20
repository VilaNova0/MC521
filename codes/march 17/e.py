def check_anagram(w1: str, w2: str) -> bool:
    if len(w1) != len(w2):
      return False

    counts = {}
    for c1, c2 in zip(w1.lower(), w2.lower()):
        if c1 in counts.keys():
            counts[c1] += 1
        else:
            counts[c1] = 1
        if c2 in counts.keys():
            counts[c2] -= 1
        else:
            counts[c2] = -1

    for count in counts.values():
        if count:
            return False
    return True

words = []

while True:
    line = input()
    if line == '#':
        break
    words.extend(line.split())

anagrams = [x for x in words]
for i in range(len(words)):
    for j in range(len(words)):
        if i == j:
            continue
        if check_anagram(words[i], words[j]):
            anagrams.remove(words[i])
            break

for anagram in sorted(anagrams):
    print(anagram)