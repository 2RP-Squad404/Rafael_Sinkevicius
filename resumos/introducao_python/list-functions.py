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