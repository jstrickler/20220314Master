from collections import Counter

with open('DATA/words.txt') as words_in:
    first_letters = [word[0] for word in words_in]

first_letter_counts = Counter(first_letters)

first_letter_counts['wombat'] += 1
first_letter_counts['wombat'] += 1
first_letter_counts['wombat'] += 1

print("first_letter_counts: {}".format(first_letter_counts), '\n')

print(first_letter_counts.most_common(5), ' \n')


with open('DATA/breakfast.txt') as breakfast_in:
    all_food = [b.rstrip() for b in breakfast_in]
print("all_food: {}".format(all_food))

food_counts = Counter(all_food)
print("food_counts: {}\n".format(food_counts))




