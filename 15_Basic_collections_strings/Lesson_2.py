# Task 1. Improved Linguistics 2
#
# three_words_list = input('Enter three words separated by commas: ').split(', ')
# text = input('Enter the text: ')
# for word in three_words_list:
#     print('word {word} uses in text for {count} times'.format(word=word, count=text.count(word)))


# Task 2. Grandmother
#
# message = input('Enter the message: ').split()
# str_message = ' '.join(message)
# print('Fixed text: {text}'.format(text=str_message))


# Task 3. Splitters of symbols

while True:
    pattern_of_congratulations = input('Enter congratulations pattern (must contain structures: {name} and {age}): ')
    if '{name}' and '{age}' in pattern_of_congratulations:
        break
    print('Error: must contain structures: {name} and {age}.')

list_people = input('Enter list of people separated by commas: ').split(', ')
ages_list = input('Enter age of people separated by spaces: ').split()

congratulations = [pattern_of_congratulations.format(name=list_people[i], age=ages_list[i])
                   for i in range(len(list_people))]

print('\n'.join(congratulations))

print('\nBirthday people: ', end='')
for i in range(len(list_people)):
    print(' '.join([list_people[i], ages_list[i]]), end=', ')

