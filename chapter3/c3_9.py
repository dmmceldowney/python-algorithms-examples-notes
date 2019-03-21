from c_3_5stack import Stack

def infixToPostfix(infixepr):
    prec = {} # precedence
    prec["**"] = 4 # this was the only change we needed to make to answer the question at the end
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    operator_stack = Stack()
    postfix_list = []
    token_list = infixepr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            top_token = operator_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = operator_stack.pop()
        else:
            while (not operator_stack.isEmpty()) and (prec[operator_stack.peek()] >= prec[token]):
                postfix_list.append(operator_stack.pop())
            operator_stack.push(token)

    while not operator_stack.isEmpty():
        postfix_list.append(operator_stack.pop())
    return " ".join(postfix_list)


def doMath(op, op_1, op_2):
    if op == '*':
        return op_1 * op_2
    elif op == '/':
        return op_1 / op_2
    elif op == '+':
        return op_1 + op_2
    elif op == '-':
        return op_1 - op_2


def postfix_eval(postfix_expr): #postfix_expression
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in '1234567890':
            operand_stack.push(int(token))
        else:
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()

            result = doMath(token, operand_1, operand_2)
            operand_stack.push(result)

    return operand_stack.pop()


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

print(postfix_eval('7 8 + 3 2 + /'))

# question 
print(infixToPostfix('5 * 3 ** ( 4 - 2 )'))






