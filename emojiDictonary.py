def emojiStatement(message):
    words = message.split(" ")
    emojiDict = {
        ':)': "😃",
        ":(": "😞"
    }

    output = ''

    for word in words:
        output += emojiDict.get(word, word) + ' '
    return output


message = input(">")


print(emojiStatement(message))