import ast
import sys

import operator as op

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv,ast.USub: op.neg}
symbolTable = {}

# function to evaluate the expressions from the abstract syntax tree.
# will evaluate binary and unary operators down the tree till child nodes through recursion,
# it will return the value if its a number or variable
def evaluate(node):
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node,ast.Name):
        return symbolTable[node.id]
    elif isinstance(node, ast.BinOp):
        return operators[type(node.op)](evaluate(node.left), evaluate(node.right))
    elif isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](evaluate(node.operand))

code = open(sys.argv[1],"r") # change the file for giving a different input

for line in code:
    if(line!='\n'):
        # in the given grammar only two types of expressions are possible. an assignment and a print statement.So handled these two
        #cases only
        a = ast.parse(line,mode='exec')
        if(isinstance(a.body[0],ast.Assign)):
            symbolTable[a.body[0].targets[0].id] = evaluate(a.body[0].value) #need to store the computed variable for further use
        elif (isinstance(a.body[0],ast.Print)):
            print evaluate(a.body[0].values[0])
