from pprint import pprint

letter_counts = {}

with open('DATA/words.txt') as words_in:
    for raw_word in words_in:
        word = raw_word.rstrip()
        if len(word) == 5:
            first_letter = word[0]

            if first_letter in letter_counts:
                letter_counts[first_letter] += 1
            else:
                letter_counts[first_letter] = 1

pprint(letter_counts)
