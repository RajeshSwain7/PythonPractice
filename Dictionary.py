#ceating a Dictionary
friend = {'name': 'John', 'age': 30, 'city': 'New York'}
print(friend)

#retriving, modifying, and adding elements in the dictionary
friend = {'name': 'John', 'age': 30, 'city': 'New York'}
print(friend)
#retriving the value of a key
#syantax-> dictionary_name[key]
print(friend['name'])  #John

#e.g-2
friends = {'tom': '111-222-333', 'jerry': '666-33-111'}
print(friends)
#retreiving the value of a key
print(friends['tom'])  #111-222-333

#adding the value of a key
#syantax-> dictionary_name[key] = value
friends['bob'] = '555-444-333'
print(friends)

#modifing the value of a key
#syantax -> dictionary_name[key] = value
friends['tom'] = '444-555-666'
print(friends)
#removing a key
#syantax -> del dictionary_name[key]
del friends['tom']
print(friends)
#checking if a key exists in the dictionary
#syantax -> key in dictionary_name
print('tom' in friends)  #False
print('bob' in friends)  #True
#iterating over the keys in a dictionary
#syantax -> for key in dictionary_name
friends = {'a': '100', 'b': '200', 'c': '300', 'd': '400'}
for x in friends:
  print(friends[x])

#iterating over the keys and values in a dictionary
#syantax -> for key, value in dictionary_name.items():

for x in friends:
  print(x, friends[x])

# another way to iterate over the keys and values in a dictionary
for key, value in friends.items():
  print(key, value)

#length of the dictionary
#syantax -> len(dictionary_name)
print(len(friends))

#equality check between dictionary
#syantax -> dictionary_name == dictionary_name
friends1 = {'a': '100', 'b': '200', 'c': '300', 'd': '400'}
friends2 = {'a': '100', 'd': '400', 'c': '300', 'b': '200'}
print(friends1 == friends2)  #true
#!=
#syantax -> dictionary_name != dictionary_name
print(friends1 != friends2)  #false
#dictonary Method
#popitem()
#syantax -> dictionary_name.popitem()
#removes and returns the last key-value pair from the dictionary
friends = {'a': '100', 'b': '200', 'c': '300', 'd': '400'}
print(friends.popitem())
#pop()
#synatx -> dictionary_name.pop(key)
#removes the key-value pair with the specified key from the dictionary
fri = {'a': '100', 'b': '200', 'c': '300', 'd': '400'}
fri.pop('a')
print(fri)
#clear()
#syantax -> dictionary_name.clear()
#removes all the key-value pairs from the dictionary
fri.clear()
print(fri)

#keys()
#syantax -> dictionary_name.keys()
#returns a list of all the keys in the dictionary
fri = {'a': '100', 'b': '200', 'c': '300', 'd': '400'}
print(fri.keys())

#values()
#syantax -> dictionary_name.values()
#returns a list of all the values in the dictionary

fri = {'a': '100', 'b': '200', 'c': '300', 'd': '400'}
print(fri.values())
#get()
#syantax -> dictionary_name.get(key)
#returns the value of the key if the key exists in the dictionary
fri = {'a': '100', 'b': '200', 'c': '300', 'd': '400'}
print(fri.get('a'))
