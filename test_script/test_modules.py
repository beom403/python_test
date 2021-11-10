# python math module

# import math
# it is better importing what you use.
from math import ceil, copysign, fabs

# you can make alias
from math import fsum as alias_sum

# you can import custom modules
from code_challenge1 import plus

print(ceil(1.4))
print(copysign(1.4, -3))
print(fabs(-123))
print(alias_sum((1, 2, 3)))
print(plus(1, 3))