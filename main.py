
inputvalues = input('Enter all elements values: ')
numbers = inputvalues.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
# print ("The original list: ", numbers)

#  evenlist = [ numbers.pop(i) for i in range(len(numbers)/2)]
# evenlist = [ i for i in range(0, len(numbers), 2)]
evenlist = []
for i in range(0, len(numbers)//2):
    print(i)
    evenlist.append(numbers.pop(i))

# print ('The original list after pop() even index elements\n', numbers )
# print ("The new list from the even index elements of original list\n", evenlist)
print("The list numbers: ", numbers)
print("The list for even index elements: ", evenlist)


# .
