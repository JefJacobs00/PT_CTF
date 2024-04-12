file = open("wordlist.10000")
words = file.read().split('\n')

file2 = open("wordlist.filtered", "w")
for word in words:
    if 5 == len(word):
        file2.write(f"{word}\n")

