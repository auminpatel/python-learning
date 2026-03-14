numbers = [1, 2, 6, 5, 3, 4, 5]


numbers2 = numbers.copy()

numbers.append(6) # add to last

numbers.insert(1, 7)  # index , item


#numbers.remove(1) # item to be removed

# numbers.clear() # clears all numbers

numbers.pop() # removes the last item in the array

numbers.index(1)
print(numbers.index(1) ) # index of the first occurance of number

print(5 in numbers) # check if the number is present safer to use over index
print (8 in numbers)

print(numbers.count(5))  # total occurances of a number
print(numbers)

numbers.sort()

print(numbers)

numbers.reverse()
print(numbers)


print(numbers2)
print(numbers)