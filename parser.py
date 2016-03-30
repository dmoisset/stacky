
import token, tokenize
from ast import literal_eval

from opcodes import Operator, Opcode

def error(tok):
    print("Unknown token:", token.tok_name[tok.type], tok[1])

NAMED_OPERATORS = {
    "and": Operator.and_,
    "or": Operator.or_,
    "not": Operator.not_,
}

OPERATORS = {
    "+": Operator.plus,
    "-": Operator.minus,
    "*": Operator.mul,
    "/": Operator.div,
    "<": Operator.lt,
    ">": Operator.gt,
    "<=": Operator.le,
    ">=": Operator.ge,
    "==": Operator.eq,
    "!=": Operator.ne,
}

def parse(input):
    result = []
    lexer = tokenize.tokenize(input.readline)
    for tok in lexer:
        if tok.type in (tokenize.ENCODING, tokenize. ENDMARKER, tokenize.NL, tokenize.NEWLINE):
            pass
        elif tok.type == tokenize.NUMBER:
            result.append((Opcode.push, literal_eval(tok[1])))
        elif tok.type == tokenize.NAME:
            name = tok[1]
            if name in NAMED_OPERATORS:
                result.append((Opcode.oper, NAMED_OPERATORS[tok[1]]))
            elif name == "print":
                result.append((Opcode.print, None))
            else:
                error(tok)
        elif tok.type == tokenize.OP:
            name = tok[1]
            if name in OPERATORS:
                result.append((Opcode.oper, OPERATORS[tok[1]]))
            else:
                error(tok)
        else:
            error(tok)
    return result

if __name__ == "__main__":
    import sys
    p = parse(open("test.st", "rb"))
    print(p)

