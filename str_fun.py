#strings in python:String Functions in Python
word = 'edystiscool'

new_word = word.capitalize()
print(new_word)
# Output: Edystiscool

print (word.count('s')) # count of the s in the given variable
# Output: 2

print(word.endswith('ool'))
# Output: True

print(word.startswith('ool'))
# Output: False

print(word.startswith('edyst'))
# Output: True

print(word.startswith('hi'))
# Output: False

print(word.find('edyst')) # finds index of edyst in the given word
# Output: 0

print(word.find('edyst', 5,10)) # finds edyst in the position 5 to 10
# Output: -1

print(word.index('cool')) # index of the word cool in given variable
# Output: 7

new_word = '123abc'
print(new_word.isalnum())
# Output: True

print(word.isalpha())
# Output: True

new_word = ''
new_word = new_word.join(['edyst','is','super','cool']) # Joins all the words in the list

print(new_word)
# Output: edystissupercool
