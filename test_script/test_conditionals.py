# python conditionals

# if, else

# truth value testing

# Boolean operations - and, or, not
# {x and y} => This is a short-circuit operator, so it only evaluates the second argument if the first one is false.
# {x or y} => This is a short-circuit operator, so it only evaluates the second argument if the first one is true.
# {not x} => not has a lower priority than non-Boolean operators, so not a == b is interpreted as not (a == b), and a == not b is a syntax error.

# Comparisons
# is - object identity
# is not - negated object identity

def test_func(a, b):
    if type(b) is (int or float):
        return a + b
    else:
        print("type of b must be number")
        return None

# if elif else

def age_check(age):
    print(f"you are {age}old")
    if age < 18:
        print("you can't drink")
    elif age < 20:
        print("you are new to this")
    else:
        print("enjoy your drink")

print(test_func(1, 2))
print(test_func(1, "2"))
age_check(17)
age_check(19)
age_check(30)




