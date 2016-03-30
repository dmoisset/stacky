# Stack based language
# Evaluator function

from opcodes import Opcode, Operator

# The stack will be represented with a list and the top of the stack
# will be the last element of the list.
def evaluator(program):
    stack = []
    vardict = {}
    for i in range(len(program)):
        instruction = program[0][0]
        argument = program[0][1]

        if instruction == Opcode.push: # insert value
            stack.append(argument)
        elif instruction == Opcode.let: # create variable
            vardict[argument] = stack[-1]
        elif instruction == Opcode.get: # read variable
            stack.append(vardict[argument])
        elif instruction == Opcode.print: # view the top of stack
            print(stack[-1])
        elif instruction == Opcode.oper: # operators + - * / neg lt gt eq ne
                                         # le ge and_ or_ not_
            if argument == Operator.plus:
                stack.append(stack[-2] + stack[-1])
            elif argument == Operator.minus:
                temp = stack[-2] - stack[-1]
                del stack[-1]
                del stack[-1]
                stack.append(temp)
            elif argument == Operator.mul:
                temp = stack[-2]*stack[-1]
                del stack[-1]
                del stack[-1]
                stack.append(temp)
            elif argument == Operator.div:
                temp = stack[-2]/stack[-1]
                del stack[-1]
                del stack[-1]
                stack.append(temp)
            elif argument == Operator.lt:
                if stack[-2] < stack[-1]:
                    del stack[-1]
                    del stack[-1]
                    stack.append(True)
                else:
                    del stack[-1]
                    del stack[-1]
                    stack.append(False)
            elif argument == Operator.gt:
                if stack[-2] > stack[-1]:
                    del stack[-1]
                    del stack[-1]
                    stack.append(True)
                else:
                    del stack[-1]
                    del stack[-1]
                    stack.append(False)
            elif argument == Operator.eq:
                if stack[-2] == stack[-1]:
                    del stack[-1]
                    del stack[-1]
                    stack.append(True)
                else:
                    del stack[-1]
                    del stack[-1]
                    stack.append(False)
            elif argument == Operator.ne:
                if stack[-2] != stack[-1]:
                    del stack[-1]
                    del stack[-1]
                    stack.append(True)
                else:
                    del stack[-1]
                    del stack[-1]
                    stack.append(False)
            elif argument == Operator.le:
                if stack[-2] <= stack[-1]:
                    del stack[-1]
                    del stack[-1]
                    stack.append(True)
                else:
                    del stack[-1]
                    del stack[-1]
                    stack.append(False)
            elif argument == Operator.ge:
                if stack[-2] >= stack[-1]:
                    del stack[-1]
                    del stack[-1]
                    stack.append(True)
                else:
                    del stack[-1]
                    del stack[-1]
                    stack.append(False)
            elif argument == Operator.and_:
                temp = stack[-1] and stack[-2]
                del stack[-1]
                del stack[-1]
                stack.append(temp)
            elif argument == Operator.or_:
                temp = stack[-1] or stack[-2]
                del stack[-1]
                del stack[-1]
                stack.append(temp)
            elif argument == Operator.not_:
                if stack[-1] == True:
                    stack[-1] = False
                elif stack[-1] == False:
                    stack[-1] = True
        del program[0]
