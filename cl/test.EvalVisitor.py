import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from EvalVisitor import EvalVisitor
msg = input('? ')
input_stream = InputStream(msg.replace(" ", ""))
lexer = SkylineLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SkylineParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))
visitor = EvalVisitor({})
sky = visitor.visit(tree)
print(sky.getArea(), sky.getAlcada())
