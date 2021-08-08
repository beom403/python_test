# tuple : python's immutable sequence type.

day_tuple = ('Mon', 'Tue', 'Wed', 'Thur')

print(day_tuple)
print(day_tuple[1])
# day_tuple[1] = 'asdf'
# print(day_tuple[1])

# dictionary = key + value (like json)

johanson = {
    "name": "johanson",
    "age": 40,
    "country": "USA",
    "favorite_food": ["Kimch", "Stake"],
    "movies": ("avengers", "black widow")
}

print(johanson)

# on python, sequence type can have many types ex) string, number, list, ...

multi_type_list = ['hello', "hi", "name", [1, 2, 3], 3.1425]

print(multi_type_list)
