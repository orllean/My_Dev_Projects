all_done = '-' * 30
# chapter 1
# Why program - Python as a language

# chapter 2
# Variables expressions and statements
# constants
print('hello'.capitalize(), 'word!'.capitalize())
# You cannot use reverved words as variables names
# variable: must star with a letter or underscore, It's case sensitive
a = 35
b = 12.5
c = a * b
print(c)
# use Mnemonic names in variable
hours = 35
rate = 12.5
pay = hours * rate
print(pay)
# sentences or lines
x = 1         # assingnment statement
print(x)      # print statement
x += 1        # assingnment with expression
print(x)
# numeric expressions
# + add; - sub; * mul; / div; ** power; % remainder
x = 2
x = x + 2
print(x)
y = 440 * 12
print(y)
z = y / 1000
print(z)
x = 23
y = x % 5
print(y)
# operator procedence rules
x = 1 + 2 ** 3 / 4 * 5
print(x)
# variables type
name = 'hello word'
age = 50
male = True
print(type(name), type(age), type(male))
# type conversions
print(float(99) + 100)
i = 42
print(type(i))
f = float(i)
print(f)
print(type(f))
# strings conversions
s = '123'
print(s, type(s))
# print(s + 1)
# there will be a error if the string doesn't contain a numeric caracteres
print(int(s) + 1, type(int(s)))

# chapter 3
# conditional execution
# operators: < lass than; <= lass than or equal to; > greader than; >= greader than or equal; != no equal; == equal to
# indentention is must have
x = 5
if x > 2:
    print('greadre than 2')
    print('still bigger')
print('done with 2')
for i in range(5):  # range up to 5 but less than it.
    print(i)
    if i > 2:
        print('greader than 2')
    print('done with i', i)
print('all done')
# TRY / EXCEPT
# surround a dangerous section.
# If the code in the trys works - the except skipped
# If the code in the trys fails - it jumps to except section
x = '-'
try:
    x = int(x)
except:
    x = -1
if x > 0:
    print(f'The double of {x} is: {x * 2}')
else:
    print('x is not a number')

# chapter 4
# functions
# stored and reused
# two types: bult-in: print(), int(), etc and define by user
# define a function by use "def" maybe with arguments as imputs and invoke them by call ypur function name, parentheses and arguments in a expression
# void function - a function what does not return a value. 'not fruitful'


def print_lyrics(p_name, s_name, year):
    print((p_name.lower()).capitalize(), (s_name.lower()).capitalize())
    print(year)


print_lyrics('ORLEAN', 'coSta', 1971)
print(max(name))


def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')


greet(0)
greet('fr')
greet('es')  # print(greet('es'), 'Sally') This don't work
# a function what does return a value. 'are fruitful'
# return values


def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


print(greet('es'), 'Sally')
print(greet('fr'), 'Glenn')
print(greet('us'), 'Michael')

# chapter 5
# loops and iterations
# while - indefinite loops
n = 5
while n > 0:
    print(n)
    n -= 1
print('done')
print(n)
# breaking out of a loop
while True:
    l = 'done'  # input('> ')
    if l == 'done':
        break
    print(l)
print('all done')
# finishing an iteration with: continue
while True:
    l = 'done'  # input('> ')
    if l[0] == '#':
        continue
    if l == 'done':
        break
    print(l)
print('all done')
# for - definite loops
# must have a list of
for i in [5, 4, 3, 2, 1]:
    print(i)
print('all done')
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy new year:', friend)
print(all_done)
# loop through a set
loop_list = [9, 41, 12, 3, 74, 15]
'''
for i in loop_list:
  print(i)
print(all_done)
'''
# what is the largest number?
n = None
for i in loop_list:
    if n == None:
        n = i
    elif i > n:
        n = i
    print(i, n)
print(f'what is the largest number? {n}')
print(all_done)
# what is the lowest number?
n = None
for i in loop_list:
    if n is None:  # is operators: cam be used in logical expressions. is not also is a logical operator
        n = i
    elif i < n:
        n = i
    print(i, n)
print(f'what is the lowest number? {n}')
print(all_done)
# summing ina loop
total = 0
for i in loop_list:
    total = total + i
    print(i, total)
print(f'The total is: {total}')
print(f'The average is: {total/len(loop_list)}')
print(all_done)

# chapter 6
# strings
# we can get at any single character by use index  in square brakts.
# It's stars at zero
# loop through strings using while staement
fruit = 'banana maça'
i = 0
while i < len(fruit):
    print(i, fruit[i])
    i += 1
print(all_done)
# loop through strings using for staement
# much more elegant
for letter in fruit:
    print(letter)
print(all_done)
# loop and counting
count = 0
for letter in fruit:
    if letter.lower() == 'a':
        count += 1
print(f'The word {fruit} has {count} letter [A]')
print(all_done)
# slicing strig [start : end]
s = 'monty-python'
n = 0
for i in s:
    print(n, i)
    n += 1
print(all_done)
# if without the frist one it's starts from 0.
# the second one is the index but not include
print(s[:5])
print(s[5:6])
print(s[6:])
print(s[:])
print(all_done)
# using in as a logical operator
if 'w' not in fruit:
    print('not found it')
print(all_done)
if 'ana' in fruit:
    print('found it')
print(all_done)
# strigs library - python has a number of functions
# by invloke them appending to the string
# It's return a copy of the string altered
print(fruit.upper())
print(fruit.capitalize())
print(all_done)
# This command show all methods of the this type object (string)
all_method = dir('s')
# for i in all_method:
#   if '__' not in i:
#     print(i)
# print(all_done)
# another way
method = []
for i in all_method:
    if '__' not in i:
        method.append(i)
print(method)
print(all_done)
# another way
method = []
for e in range(0, len(all_method)):
    if '__' not in all_method[e]:
        method.append(all_method[e])
print(method)
print(all_done)
# useful stings methods
name = ' orlean ALMEIDA costa     '
print(name)
# find() search for a sustring within another string
# finds the first ocurrence. If don't -1
print(name.find('z'))
print(name.find(' '))
# upper all string
print(name.upper())
# lower all string
print(name.lower())
# captalize the first letter of the string
print((name.upper()).capitalize())
# replace all match value for other one
print(name.replace(' ', '-'))
# stripping whitespace (tab, , new line or blank)
print(name.lstrip())  # left space
print(name.rstrip())  # right space
print(name.strip())  # left and right space
# prefixes
print(name.startswith(' '))
# parsing and extrating
data = 'de:	faturacoelba@neoenergia.com por  gmail.com \nresponder a:	Nao responda <no-reply@nos.com> \npara:	rosaraamos67@gmail.com \ndata:	12 de nov. de 2021 13:22 \nassunto:	Fatura Coelba'
s = data.find('@')
e = data.find(' ', s)
print(data[(s + 1):e])

# chapter 7
# reading files
