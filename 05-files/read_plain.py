
plain = open('plain.txt')

lines = plain.readlines()

words = 0
for line in lines:
    line = line.strip()
    line_words = line.split()
    words += len(line_words)
    print(line)

print("WORDS", words)