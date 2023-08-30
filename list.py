#Python:Methods of lists
shopping_list = ['milk', 'eggs', 'cookies', 'bread'] 
shopping_list.append('chocolates')
print(shopping_list)
# Output: ['milk', 'eggs', 'cookies', 'bread', 'chocolates']

fruits_list = ['apples', 'bananas', 'oranges']
shopping_list.extend(fruits_list)
print(shopping_list)
# Output: ['milk', 'eggs', 'cookies', 'bread', 'chocolates', 'apples', 'bananas', 'oranges']

shopping_list.insert(1,'bread')
print(shopping_list)
# Output: ['milk', 'bread', 'eggs', 'cookies', 'bread', 'chocolates', 'apples', 'bananas', 'oranges']

shopping_list.remove('cookies')
print(shopping_list)
# Output: ['milk', 'bread', 'eggs', 'bread', 'chocolates', 'apples', 'bananas', 'oranges']

print(shopping_list.index('bread'))
# Output: 1

print(shopping_list.count('bread'))
# Output: 2

shopping_list.pop(3)
print(shopping_list)
# Output: ['milk', 'bread', 'eggs', 'chocolates', 'apples', 'bananas', 'oranges']

print(len(shopping_list))
# Output: 7

del shopping_list[3:5]
print(shopping_list)
# Output: ['milk', 'bread', 'eggs', 'bananas', 'oranges']

print(shopping_list[1:3])
# Output: ['bread', 'eggs']
