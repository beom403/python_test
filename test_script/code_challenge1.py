# plus
# minus
# times
# division
# negation
# power
# remainder

def plus(a, b):
    return int(a) + int(b)

def minus(a, b):
    return int(a) - int(b)

def times(a, b):
    return int(a) * int(b)

def division(a, b):
    return int(a) / int(b)

def negation(a, b):
    return -int(a), -int(b)

def power(a, b):
    return int(a) ** int(b)

def remainder(a, b):
    return int(a) % int(b)



print(plus("1", 2))
print(minus("4", 2))
print(times("4", 2))
print(division("4", 2))
print(negation("4", 2))
print(power("4", 2))
print(remainder("4", 2))
