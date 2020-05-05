# Python Program to Check Whether a String is Palindrome or Not

string = 'dad'

string = str.casefold(string)
reverse = reversed(string)

if list(string) == list(reverse):
    print('palindrome')
else:
    print('not')
