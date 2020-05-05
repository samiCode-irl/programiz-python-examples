# Python Program to Count the Number of Each Vowel
vowels = 'aeiou'
ip_str = 'Hello, have you tried our tutorial section yet?'

sent = ip_str.casefold()

count = {}.fromkeys('vowels', 0)

for letter in sent:
    if letter in count:
        count[letter] += 1

print(count)
