from utils import math_utils, string_utils
#Numbers: '34' and '45'
a = 34
b = 45

print("Addition:", math_utils.add(a, b))
print("Subtraction:", math_utils.sub(a, b))
print("Multiplication:", math_utils.mul(a, b))
print("Division:", math_utils.div(a, b))
print("Remainder:", math_utils.rem(a, b))

# Strings: 'BDBH' and '101'
s1 = "BDBH"
s2 = "101"

print("Uppercase:", string_utils.to_upper(s2))
print("Lowercase:", string_utils.to_lower(s1))
print("Concatenation:", string_utils.to_concatenate(s1, s2))