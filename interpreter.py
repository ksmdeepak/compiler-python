import ast
import sys

import operator as op

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
                 ast.Div: op.truediv,ast.USub: op.neg}
symbolTable = {}

class Interpreter:
    # function to evaluate the expressions from the abstract syntax tree.
    # will evaluate binary and unary operators down the tree till child nodes through recursion,
    # it will return the value if its a number or variable
    def evaluate(self,node):
        if isinstance(node, ast.Num):
            return node.n
        if isinstance(node,ast.Name):
            return symbolTable[node.id]
        elif isinstance(node, ast.BinOp):
            return operators[type(node.op)](self.evaluate(node.left), self.evaluate(node.right))
        elif isinstance(node, ast.UnaryOp):
            return operators[type(node.op)](self.evaluate(node.operand))
        else:
            raise Exception

    def compute(self,fileName):
        code = open(fileName, "r")  # change the file for giving a different input
        output = []
        for line in code:
            if (line != '\n'):
                # in the given grammar only two types of expressions are possible. an assignment and a print statement.So handled these two
                # cases only
                a = ast.parse(line, mode='exec')
                if (isinstance(a.body[0], ast.Assign)):
                    symbolTable[a.body[0].targets[0].id] = self.evaluate(a.body[0].value)  # need to store the computed variable for further use
                elif (isinstance(a.body[0], ast.Print)):
                    print self.evaluate(a.body[0].values[0])
                    output.append(self.evaluate(a.body[0].values[0]))

        return output

if __name__ == '__main__':
    Interpreter().compute(sys.argv[1])
