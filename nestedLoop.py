for x in range(11):
    for y in range(10):
        print(f'{x} , {y}')


numbers = [5,2,5,2,2]

for item in numbers:
    string = ''
    for i in range(item):
        string += 'x'

    print(string)