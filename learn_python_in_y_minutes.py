# Learn x in y minutes, where x = python
# rewriting it in a way that makes sense to me, plus extra side notes
# typing muscle memory

# Single line comments
""" Multi-line
    comments
    like
    this
"""

# 1. Datatypes and operators
# string, integer, float, boolean
# +, -, *, /


# returns the quotient either position or negative, no floats/remainder
    # rounds DOWN, so if the answer is 0.666 => 0, or 1.66666 => 1
5 // 3 # => 1
-5 // 3 # => -2

#  modulo counts how many remainders you have left
#  example: if i had 6 cookies and 4 friends, if everyone got a cookies
    # including me, which would make 5, I would have 1 cookie left.
7 % 3 # => 1

# Boolean - make sure they are capitalized Ruby was lowercase
True
False

# Boolean operators Ruby(&&, ||, !)
and # True and True => True
or # False or True => True
not # !False = > True

# Using Bool operators with int, 0 => False, 1 => True
0 and 2 # => 0
2 == True # => False
1 == True # => True


#  is vs. ==
# checks if two variables refer to the same object
# but == checks if the objects have the same values

a = [1,2,3,4]
b = a
b is a # True
b == a # True
b = [1,2,3,4]
b is a # False, a and b do not refer to the same object
b == a # True, objects are equal

# Strings can be added WITHOUT '+'
"Hello" "world!" # "Hello world!"
# the example had "Hello " <= extra space,
# tested it you just need "Hello" no space

# .format can be used to format strings:
# Ruby had #{variable_name}
"{} can be {}".format("Strings", "interpolated")
# "Strings can be interpolated"


# Can repeat arguments
"{0} can be cold, {0} can be warm, {0} can be cloudy, \
all in one day unless it {1}.".format("SF", "rains")
# "SF can be cold, SF can be warm, SF can be cloudy, all in one day
    # unless it rains."

# Just learned "\" is a line break for when your code is too long


# can use keywords too
"{name} wants to eat {food}".format(name="Mira", food="crawfish")
# "Mira wants to eat crawfish"


# None is an object
None # => None

# Don't use "==" to compare ojbects to None use "is"
# This checks for equality of object identity
"etc" is None # => False
None is None # => True
