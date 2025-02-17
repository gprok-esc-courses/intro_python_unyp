
sentence = "This is a senetence to count character frequency"
sentence = sentence.lower()

letter_dict = {}

for ch in sentence:
    if ch != ' ':
        if ch in letter_dict:
            letter_dict[ch] += 1
        else:
            letter_dict[ch] = 1

for x in letter_dict:
    print(x, letter_dict[x])
