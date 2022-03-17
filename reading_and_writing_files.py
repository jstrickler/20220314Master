FILE_PATH = 'DATA/mary.txt'

mary_in = open(FILE_PATH, 'r')  # linux/mac abs path:  /Users/jstrick/Desktop/py3master/DATA/mary.txt
# windows abs path    C:\  \\drive_name
#  read file here ...
mary_in.close()

# read one line at a time into a string
with open(FILE_PATH) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove \n from end of line
        # print("raw:", repr(raw_line))
        # print("stripped:", repr(line))
        print(line)
        print()
print('-' * 60)

# read entire file into a string
with open(FILE_PATH) as mary_in:
    contents = mary_in.read()
    print("RAW:")
    print(repr(contents))
    print("NORMAL:")
    print(contents)
print('-' * 60)

# read file into list of lines with newlines
with open(FILE_PATH) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

# read file into list of lines without newlines
with open(FILE_PATH) as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)


total_word_count = 0
target_word_count = 0
target = 'x'
output_file = f"{target}_words.txt"
with open('DATA/words.txt') as words_in:
    with open(output_file, 'w') as words_out:  # save to x_words.txt on filesystem
        for word in words_in:
            total_word_count += 1
            if word[0] == target:    # if word.startswith('x')
                target_word_count += 1
                words_out.write(word)  # .write(...) takes 1 string

percentage = (target_word_count / total_word_count) * 100
print(f"{target_word_count} words start with '{target}' ({percentage}%)")

#  modes:  'r' 'w' 'a' 'x'

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')


