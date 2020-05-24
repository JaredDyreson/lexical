#!/usr/bin/env python3.8

import operands

"""
Needed components:
  - Enumeration class deciding which operands we need to use
  - Expression to iterate over
  - Function map to allow us correspond an operand to an instruction from Python
"""

class lexer():
    def __init__(self, operands):
        self.operands = operands
        self.operands_names_ = [operand.name for operand in self.operands]

    def is_keyword(self, pattern: str) -> bool:
        """
        Check if given token given is a keyword.
        If it is, then we cannot use it for variable assignment.
        """
        return pattern in self.operand_names_

    def individual_token(self, token: str) -> int:
        """
        Iterate over the token names.
        If there is a match, return it's operand code.
        If there is not a match, return a garbage value.
        """
        if(token in self.operands_names_):
          return getattr(self.operands, token).value
        return self.operands.GARBAGE.value

    def tokenize(self, expression: str) -> list:
        """
        Iterate over an expression and return a list of tokens
        This list can then be used to interface with a function map
        """
        token_list = []
        for index, token in enumerate(expression.split()):
          try:
            token_list.append(self.individual_token(token))
          except Exception as error:
            print("Malformed expression: \"{}\" at token \'{}\' (index: {})".format(expression, token, index))
            break
        return token_list

    def execute(self, expression: str, function_map: dict) -> None:
        """
        Given an expression and a function map, we can iterate over a string and perform operations directly
        We will show where the error occurred and the Exception raised
        """
        expression_split = expression.split()
        for index, token in enumerate(self.tokenize(expression)):
            try:
              function_map[token](expression_split[index])
            except Exception as error:
              print("Malformed expression: \"{}\" at token \'{}\' (index: {})".format(expression, token, index))
              print("[-] Error received: {}".format(error))
              break


# example usage

# def list_all(token: str):
  # print("I will list them all: {}".format(token))

# expression = "this is a line LIST HELLO"
# lex = lexer(operands.OperandCodes)

# function_map = {
    # lex.operands.GARBAGE.value: lambda token: print("Got a garbage value of {}".format(token)) ,
    # lex.operands.LIST.value: lambda token: list_all(token)
# }

# lex.execute(expression, function_map)
