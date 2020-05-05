# Python Program to Remove Punctuations From a String

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, he said ---and went."

no_punct = ''

for s in my_str:
    if s not in punctuations:
        no_punct += s

print(no_punct)
