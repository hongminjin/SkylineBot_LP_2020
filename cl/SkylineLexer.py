# Generated from Skyline.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\7\4$\n\4\f\4\16\4\'\13\4")
        buf.write("\3\5\6\5*\n\5\r\5\16\5+\3\6\3\6\3\6\5\6\61\n\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\7\rT\n\r\f\r\16\rW\13\r\3\r")
        buf.write("\3\r\3\r\3\16\6\16]\n\16\r\16\16\16^\3\16\3\16\2\2\17")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\3\2\6\4\2C\\c|\5\2\62;C\\c|\3\2\62;\5\2\13\f")
        buf.write("\17\17\"\"\2f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2")
        buf.write("\t)\3\2\2\2\13\60\3\2\2\2\r\62\3\2\2\2\17\64\3\2\2\2\21")
        buf.write("\66\3\2\2\2\238\3\2\2\2\25;\3\2\2\2\27C\3\2\2\2\31O\3")
        buf.write("\2\2\2\33\\\3\2\2\2\35\36\7*\2\2\36\4\3\2\2\2\37 \7+\2")
        buf.write("\2 \6\3\2\2\2!%\t\2\2\2\"$\t\3\2\2#\"\3\2\2\2$\'\3\2\2")
        buf.write("\2%#\3\2\2\2%&\3\2\2\2&\b\3\2\2\2\'%\3\2\2\2(*\t\4\2\2")
        buf.write(")(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\n\3\2\2\2-\61")
        buf.write("\5\t\5\2./\7/\2\2/\61\5\t\5\2\60-\3\2\2\2\60.\3\2\2\2")
        buf.write("\61\f\3\2\2\2\62\63\7/\2\2\63\16\3\2\2\2\64\65\7-\2\2")
        buf.write("\65\20\3\2\2\2\66\67\7,\2\2\67\22\3\2\2\289\7<\2\29:\7")
        buf.write("?\2\2:\24\3\2\2\2;<\7*\2\2<=\5\13\6\2=>\7.\2\2>?\5\t\5")
        buf.write("\2?@\7.\2\2@A\5\13\6\2AB\7+\2\2B\26\3\2\2\2CD\7}\2\2D")
        buf.write("E\5\t\5\2EF\7.\2\2FG\5\t\5\2GH\7.\2\2HI\5\t\5\2IJ\7.\2")
        buf.write("\2JK\5\13\6\2KL\7.\2\2LM\5\13\6\2MN\7\177\2\2N\30\3\2")
        buf.write("\2\2OU\7]\2\2PQ\5\25\13\2QR\7.\2\2RT\3\2\2\2SP\3\2\2\2")
        buf.write("TW\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WU\3\2\2\2XY\5")
        buf.write("\25\13\2YZ\7_\2\2Z\32\3\2\2\2[]\t\5\2\2\\[\3\2\2\2]^\3")
        buf.write("\2\2\2^\\\3\2\2\2^_\3\2\2\2_`\3\2\2\2`a\b\16\2\2a\34\3")
        buf.write("\2\2\2\b\2%+\60U^\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    T__0 = 1
    T__1 = 2
    IDENT = 3
    NUM = 4
    INT = 5
    RES = 6
    SUM = 7
    MUL = 8
    ASSIGN = 9
    EDIF = 10
    RAND = 11
    EDIFS = 12
    WS = 13

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>", "'('", "')'", "'-'", "'+'", "'*'", "':='"]

    symbolicNames = ["<INVALID>", "IDENT", "NUM", "INT", "RES", "SUM", "MUL", "ASSIGN", "EDIF", "RAND", "EDIFS", "WS"]

    ruleNames = ["T__0", "T__1", "IDENT", "NUM", "INT", "RES", "SUM", "MUL", "ASSIGN", "EDIF", "RAND", "EDIFS", "WS"]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
