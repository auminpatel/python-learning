from phoneMumber import output

message = input(">")
words = message.split(" ")
emojiDict = {
    ':)': "😃",
    ":(": "😞"
}

output = ''

for word in words:
    output += emojiDict.get(word, word) + ' '

print(output)