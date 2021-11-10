# reference: python standard library

# class bytearray([source[, encoding[, errors]]])
# Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in Mutable Sequence Types, as well as most methods that the bytes type has, see Bytes and Bytearray Operations.

# class bytes([source[, encoding[, errors]]])
# Return a new “bytes” object, which is an immutable sequence of integers in the range 0 <= x < 256. bytes is an immutable version of bytearray – it has the same non-mutating methods and the same indexing and slicing behavior.

# basic function (positional argument)

def test_function(a, b):
    print(a, b)

# function that returns value
def test_function2(a):
    return a + 1

# keyworded argument
def test_function3(a, b):
    print("a : ", a)
    print("b : ", b)

# format string
def test_function4(name, age):
    print(f"my name is {name}, i'm {age} years old")



test_function(1, 2)
test_function2(1)
test_function3(b = "b", a = "a")
test_function4("beom", 333)

