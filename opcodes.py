from enum import Enum

Opcode = Enum('Opcode', 'push oper let get print')

Operator = Enum('Operator', 'plus minus mul div')

# program = [(Opcode.get, "x"), (Opcode.get, "y"), (Opcode.oper, Operator.plus)]
