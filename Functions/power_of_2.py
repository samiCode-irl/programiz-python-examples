# Python Program To Display Powers of 2 Using Anonymous Function

terms = 10

result = list(map(lambda x: 2 ** x, range(terms)))

for i in range(terms):
    print(f'The power of 2 of {i} = {result[i]}')
