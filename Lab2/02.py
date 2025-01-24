#                                      Operators
# Python Arithmetic Operators
b = 10
c = 3
a = b + c  #Addition        13
a = b - c  #Subtraction     7
a = b * c  #Multiplication  30
a = b / c  #Division        3.3...
a = b % c  #Modulus         1
a = b ** c #Exponentiation  1000
a = b // c #Floor division  3


#Python Assignment Operators
b = 10
c = 3           # Same as    
b += c          # b = b + c     b = 13
b -= c          # b = b - c     b = 7
b *= c          # b = b * c     b = 30
b /= c          # b = b / c     b = 3.3...
b %= c          # b = b % c     b = 1
b //= c         # b = b // 3    b = 3
b **= c         # b = b ** c    b = 30
b &= c          # b = b & c     b = 2      двоичное умножение
b |= c          # b = b | c     b = 11     двоичное сложение
b ^= c          # b = b ^ c     b = 9      двоичное xor
b >>= c         # b = b >> c    b = 1      shift right in binary
b <<= c         # b = b << c    b = 80     shift left in binary
print(b := 2)   # b = 2
                # print(b)


#Python Comparison Operators
a == b      #Equal
a != b      #Not equal
a > b       #Greater than
a < b       #Less than
a >= b      #Greater than or equal to
a <= b      #Less than or equal to


#Python Logical Operators
a < 5 and  b < 10
a < 5 or b < 4
not(a < 5 and b < 10)