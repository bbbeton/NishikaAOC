def vowel_check(word):
    counter = 0
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            counter += 1
    if counter >= 3:
        return True
    else:
        return False

def double_check(word):
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            return True
    return False

def no_bad_strings(word):
    for i in range(len(word) - 1):
        if word[i:i+2] in ['ab', 'cd', 'pq', 'xy']:
            return False
    return True

def is_nice(word):
    if vowel_check(word) and double_check(word) and no_bad_strings(word):
        return True
    else:
        return False

def double_double_check(word):
    for i in range(len(word) - 3):
        if word[i:i+2] in word[i+2:]:
            return True
    return False

def between_double_check(word):
    for i in range(len(word) - 2):
        if word[i] == word[i+2]:
            return True
    return False

def new_is_nice(word):
    if double_double_check(word) and between_double_check(word):
        return True
    else:
        return False
# ------------------------------------------------------------------------------

with open('day5.txt') as f:
    input = f.read().split("\n")

counter = 0
for word in input:
     if is_nice(word):
         counter += 1
print(counter)

counter = 0
for word in input:
     if new_is_nice(word):
         counter += 1
print(counter)

