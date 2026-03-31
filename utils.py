def findLargest(numbers):

    max = numbers[0]
    for item in numbers:
        if item > max:
            max = item

    return max
