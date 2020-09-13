
TRUE = lambda x,y: x
FALSE = lambda x,y: y

NOT = lambda x: x(FALSE,TRUE)
AND = lambda x,y: x(y,FALSE)
OR = lambda x,y: x(x,y)
IFTHENELSE = lambda x,y,z: x(y,z)

assert NOT(TRUE) is FALSE
assert NOT(FALSE) is TRUE
assert AND(TRUE,TRUE) is TRUE
assert AND(TRUE,FALSE) is FALSE
assert AND(FALSE,TRUE) is FALSE
assert AND(FALSE,FALSE) is FALSE
assert OR(TRUE,TRUE) is TRUE
assert OR(FALSE,TRUE) is TRUE
assert OR(TRUE,FALSE) is TRUE
assert OR(FALSE,FALSE) is FALSE
assert IFTHENELSE(TRUE,TRUE,FALSE) is TRUE
assert IFTHENELSE(FALSE,TRUE,FALSE) is FALSE

def incr(x):
    return x + 1
ZERO = lambda f: lambda x: x
ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
SUCC = lambda n: (lambda f: lambda x: f(n(f)(x)))
ADD = lambda x: lambda y: y(SUCC)(x)
MUL = lambda x: lambda y: lambda f: y(x(f))

print(SUCC(TWO)(incr)(0))
print(ADD(TWO)(THREE)(incr)(0))
print(MUL(TWO)(THREE)(incr)(0))