#Lists in Python

nums = [25,12,26,95,14]
print(nums)

print(nums[0])

print(nums[4])

print(nums[2:])

print(nums[-1])

print(nums[-5])

names = ['diya','kiran','john']
print(names)

#Heterogeneous list

values = [9.5, 'Divya', 25]
print(values)

#Prints lists of list

mil = nums + names
print(mil)

#Methods in python

#append(element)
nums.append(45)
print(nums)

#clear()
nums.clear()
print(nums)

#insert(index, element)
nums = [25,12,26,95,14]
nums.insert(3,44)
print(nums)

#Difference between append and insert
'''
append() - will add element at the end
insert() - It will insert the element based on index we are providing
'''

#remove(element)
nums.remove(14)
print(nums)

#pop(index)
nums.pop(1)
print(nums)

#pop() -- Without specifying index it will remove last indexed value
nums.pop()
print(nums)

nums = [25,12,36,96,14]

#del -- Delete multiple elements
del nums[2:]
print(nums)

#extend -- Add multiple values
nums.extend([23,56,78])
print(nums)

#In built functions

#min()
print(min(nums))

#max()
print(max(nums))

#sum()
print(sum(nums))

#sorted()
print(sorted(nums))

#reversed()
print(list(reversed(nums)))