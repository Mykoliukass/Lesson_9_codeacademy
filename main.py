# squares = []
# for number in range(10):
#     if number != 5:
#         squares.append(number *number)
# print(squares)

# squares = [number*number for number in range(10) if number%2 == 0]
# print(squares)

# names = ['Asilas', 'Avinas', 'Poteris', 'Drasius']
# names_with_a =[]
# for name in names:
#     if name.startswith('A'):
#         names_with_a.append(name)
# print(names_with_a)

# Find all of the numbers from 1-1000 that are divisible by 6.
# number_that_are_divisible_by_6 = [i for i in range(1,1001) if i%6==0]
# print(number_that_are_divisible_by_6)

# Find all number from 1-1000 that have 9 in them.
# number_that_have_9 = [i for i in range(1,1001) if '9' in str(i)]
# print(number_that_have_9)

# Given string: text = 'In this lecture we will review some additional functionalities of python built-in data structures.' 
# calculate how many words have letter 'e' in it.

# text = 'In this lecture we will review some additional functionalities of python built-in data structures.' 
# words_with_e = [word for word in text.split() if 'e' in word]
# num = len(words_with_e)
# print(f"Number of words with 'e': {num}")

# Given the same string as in previous exercise: calculate count of words that have more than 5 characters.

# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# long_words = [word for word in text.split() if len(word)>=5]
# num = len(long_words)
# print(f"Number of words with more than 5 characters': {num}")

# Write a program that checks if given number is a perfect square.
given_num = int(input('Please provide me with a number to check if it is a prefect square: '))
root =int(given_num **0.5)
if root **2 == given_num:
     print('It is a perfect square')
else:
    print('It is not a perfect square') 