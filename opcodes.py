from enum import Enum

Opcode = Enum('Opcode', 'push oper let get print')

Operator = Enum('Operator', 'plus minus mul div neg lt gt eq ne le ge and_ or_ not_')

# program = [(Opcode.get, "x"), (Opcode.get, "y"), (Opcode.oper, Operator.plus)]
