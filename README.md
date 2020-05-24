# lexical

A simple Python lexer.

This Python class takes in an operand class:

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
