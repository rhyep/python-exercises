# 3.2-operator-precedence-and-associativity.py

a = 2 + 3 * 4

b = (2 + 3) * 4

c = 2 + (3 * 4)

print(a, b, c)

'''
Binary      **              Right
Unary       +, -            Right
Binary      *, /, //, %     Left
Binary      +, -            Left
Binary      =               Right
'''
