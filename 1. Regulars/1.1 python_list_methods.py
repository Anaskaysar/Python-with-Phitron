
#list
#index  =  0    1   2   3   4   5   6   7   8 
numbers = [45, 10, 15, 14, 44, 34, 233, 32,93] 

#Add a single item at the end of the list
numbers.append(10)
print(numbers)

#add items in a particular place
numbers.insert(0,2)

#remove an item from a list
if 93 in numbers:
    numbers.remove(93)
print(numbers)

#pick an item from list and remove it from there, print it separate
last = numbers.pop()
print(last, numbers)

numbers2 = [45, 10, 45, 14, 44, 34, 233, 32,93] 
print(numbers2.count(45))