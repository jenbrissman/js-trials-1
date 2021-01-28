"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    # TODO: replace this line with your code
    for item in items:
        print(item)

# print(output_all_items([1, "hello", True]))

def get_all_evens(nums):
    # TODO: replace this line with your code
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

# print(get_all_evens([7, 8, 10, 1, 2, 2]))

def get_odd_indices(items):
    # TODO: replace this line with your code
    odd_indices = []
    for idx in range(len(items)):
        if idx % 2 != 0:
            odd_indices.append(items[idx])
    return odd_indices 

print(get_odd_indices([1, 'hello', True, 500]))

def print_as_numbered_list(items):
    # TODO: replace this line with your code
    i = 1
    
    for item in items:
        print (f"{i}. {item}")
        i += 1

print_as_numbered_list([1, 'hello', True])

def get_range(start, stop):
    # TODO: replace this line with your code
    nums_list = []
    for i in range(start, stop):
        nums_list.append(i)
    print(nums_list)

# get_range(0,5)

def censor_vowels(word):
    # TODO: replace this line with your code
    chars = []

    for char in word:
        if char in 'aeiou':
            chars.append('*')
        else:
            chars.append(char)

    return("".join(chars))
    
print(censor_vowels('hello world'))


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
