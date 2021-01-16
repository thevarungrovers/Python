a = "Hello world!"

print(a.lower()) # lower characters

print(a.upper()) # upper characters

print(a.replace('!','!!')) # replace something

print(a.split(' ')) # break the string to list

print(a[2]) # print character at 2 index

print(a[2:]) # print whole substring after index 2

print(a[2:7]) # print substring between 2 and 7

print(a[:5]) # print substring till index 5

print(len(a)) # length of atring

print(a.capitalize()) # each capital word of sentence

# count substring in a string
b = 'l'
print(a.count(b))

# to check end character
print(a.endswith(b))

# to check substring available in string
c = 'll'
print(a.find(c))

# alphanumeric
print(a.isalnum())

# digit
print(a.isdigit())

#alphabets
print(a.isalpha())

# numerics
print(a.isnumeric())

#whitespaces
print(a.isspace())

# each word first letter capital
print(a.istitle())

# to join a sequence with character
d = ['hello','with','python']
e = '-'
print(e.join(d))

# maximum character
print(max(a))

# minimum character
print(min(a))

# return last index where substing is found
f = 'wo'
print(a.rindex(f))  # gives exception if not found
print(a.rfind(f))

# strip character from beginning
g = '****this is example!!****'
print(g.lstrip('*'))

