phone = input('Enter your phone number: ')
digits_mapping = {
    "1": 'one',
    "2": 'two',
    "3": 'three',
    "4": 'four',
    "5": 'five',
    "6": 'six',
    "7": 'seven',
    "8": 'eight',
}

output = ""

for char in phone:
    output += digits_mapping.get(char, "!") + ' '
print(output)