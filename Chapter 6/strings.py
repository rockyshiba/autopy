# what are strings?
title = "Moby Whale"
author = 'Ahab Fish'
phone = '12-345-6789'

# They are a type and an object
print(title[1]) # i
title.upper()
title.lower()
'it' in title
title.startswith('The')

# They are immutable
# Uncommented, Python will throw an error
# title[0] = 'R'

# Remember, spaces are also strings
spaces = '      a     '
print(a.strip())

# They can be looped over
for letter in title:
    print(letter)

# Numbers can be converted to string
# Not all strings can be converted to a number

# String formatting
Description = title + ', ' + author + ', ' + phone
Description = f'{title}, {author}, {phone}'
print(f'The sum of 2 and 4 is {2+4}')