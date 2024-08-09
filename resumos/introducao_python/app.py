from math import *

print('Hello World')

print('   /|')
print('  / |')
print(' /  |')
print('/___|')

character_name = 'John'
character_age = 35
isMale = True
print('named ' + character_name)
print('he was ' + character_age)
character_name = 'Mike'
print('the name ' + character_name)
print('being ' + character_age)

phrase = 'Giraffe Academy'
print('Giraffe\nAcademy')
print(phrase + ' is cool')
print(phrase.lower() + ' is cool')
print(phrase.upper() + ' is cool')
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("G"))
print(phrase.replace('Giraffe', 'Elephant'))

my_num = 5
print(-2.0987)
print(3 + 4.5)
print(3 * (4 + 5))
print(10 % 3)
print(str(my_num) + ' my favorite number')
my_num = -5
print(abs(my_num))
print(pow(3, 2))
print(max(3, 2))
print(min(3, 2))
print(round(3.2))
print(floor(3.2))
print(ceil(3.2))
print(sqrt(32))

name = input(' enter your name: ' )
age = input('enter your age: ')
print('Hello ' + name + '! You are ' + age + ' years old!')

num1 = input('Enter a number: ')
num2 = input('Enter another number: ')
result = float(num1) + float(num2)
print(result)

color = input('enter a color ')
plural_noun = input('enter a plural noun ')
celebrity = input('enter a celebrity ')
print('roses are ' + color)
print(plural_noun + ' are blue')
print('I love ' + celebrity)

friends = ['Kevin', 'Karen', 'Jim', ' Oscar', 'Toby']
friends[1] = 'Mike'
print(friends[0])
print(friends[1:3])

lucky_numbers = [4,8,15,16,23,42]
friends = ['Kevin', 'Karen', 'Jim', ' Oscar', 'Toby']
friends.extend(lucky_numbers)
friends.append('Creed')
friends.insert(1, 'Kelly')
friends.remove('Jim')
friends.clear()
friends.pop()
friends.sort()
lucky_numbers.sort()
lucky_numbers.reverse()
friends2 = friends.copy()
print(friends.index('Kevin'))
print(friends.count('Jim'))
print(lucky_numbers)
print(friends2)
print(friends)

coordinates = [(4,5),(6,7),(80,34)]
coordinates[1] = 10
print(coordinates[1])

def sayhi(name, age):
    print('Hello '+ name + ' ,youre ' + str(age))
sayhi('Mike', 35)
sayhi('Steve', 70)

def cube(num):
    return num*num*num
result = cube(4)
print(result)

is_male = True
is_tall = True
if is_male or is_tall: 
    print('You are a male or tall or both')
else:
    print('You neither male or tall')

if is_male and is_tall: 
    print('You are a tall male')
elif is_male and not(is_tall):
    print('You are a short male')
elif not(is_male) and is_tall:
    print('You are not a male but are tall')
else:
    print('You are not a male and not tall')