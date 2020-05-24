# lexical

A simple Python lexer.


This Python class takes in three components:

- Enumeration class
- Expression
- Function map



## Enumeration Class

```python
from aenum import Enum

class OperandCodes(Enum, start=0):
    GARBAGE
    LINEFEED
```

and will use these enumerations to determine which operands to use.

The name of the instruction should be the operand name. For example, if you need your program to use `LIST`, then your class would look like this:


```python
from aenum import Enum

class OperandCodes(Enum, start=0):
    LIST
    GARBAGE
    LINEFEED
```

## Expression

These expressions are simply strings that contain instructions.

For example:

`LIST NUMBERS 1-10`

You can instruct the lexer to pick up on keywords such as `LIST` and `NUMBERS`, where you can do something with the parameter `1-10`

## Function map

These function maps have an operand code correspond to a function/operation that it signals.

An example function map can be as follows:

```python
def list_all(token: str):
  s = token.split("-")
  begin, end = s[0], s[1]
  for x in range(begin, end): print(x)

# where operand is an import that contains the class OperandCodes which is an Enumeration class, component number one
lex = lexer(operand.OperandCodes)
function_map = {
    lex.operands.GARBAGE.value: lambda token: print("Got a garbage value of {}".format(token)) ,
    lex.operands.LIST.value: lambda token: list_all(token)
}
```
