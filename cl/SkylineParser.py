# Generated from Skyline.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("@\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3\26\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\7\4\37\n\4\f\4\16\4\"\13\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\7\5)\n\5\f\5\16\5,\13\5\3\6\7\6/\n\6\f\6\16\6\62")
        buf.write("\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7>\n\7")
        buf.write("\3\7\2\2\b\2\4\6\b\n\f\2\2\2D\2\16\3\2\2\2\4\25\3\2\2")
        buf.write("\2\6\27\3\2\2\2\b#\3\2\2\2\n\60\3\2\2\2\f=\3\2\2\2\16")
        buf.write("\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2\21\26\5\6\4\2\22")
        buf.write("\23\7\5\2\2\23\24\7\13\2\2\24\26\5\6\4\2\25\21\3\2\2\2")
        buf.write("\25\22\3\2\2\2\26\5\3\2\2\2\27 \5\b\5\2\30\31\7\t\2\2")
        buf.write("\31\37\5\b\5\2\32\33\7\b\2\2\33\37\7\6\2\2\34\35\7\t\2")
        buf.write("\2\35\37\7\6\2\2\36\30\3\2\2\2\36\32\3\2\2\2\36\34\3\2")
        buf.write("\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\7\3\2\2\2\" ")
        buf.write("\3\2\2\2#*\5\n\6\2$%\7\n\2\2%)\5\n\6\2&\'\7\n\2\2\')\7")
        buf.write("\6\2\2($\3\2\2\2(&\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2")
        buf.write("\2+\t\3\2\2\2,*\3\2\2\2-/\7\b\2\2.-\3\2\2\2/\62\3\2\2")
        buf.write("\2\60.\3\2\2\2\60\61\3\2\2\2\61\63\3\2\2\2\62\60\3\2\2")
        buf.write("\2\63\64\5\f\7\2\64\13\3\2\2\2\65\66\7\3\2\2\66\67\5\6")
        buf.write("\4\2\678\7\4\2\28>\3\2\2\29>\7\f\2\2:>\7\16\2\2;>\7\r")
        buf.write("\2\2<>\7\5\2\2=\65\3\2\2\2=9\3\2\2\2=:\3\2\2\2=;\3\2\2")
        buf.write("\2=<\3\2\2\2>\r\3\2\2\2\t\25\36 (*\60=")
        return buf.getvalue()


class SkylineParser (Parser):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", "<INVALID>", "'-'", "'+'", "'*'", "':='"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "IDENT", "NUM", "INT", "RES", "SUM", "MUL", "ASSIGN", "EDIF", "RAND", "EDIFS", "WS"]

    RULE_root = 0
    RULE_expr = 1
    RULE_sky = 2
    RULE_msky = 3
    RULE_rsky = 4
    RULE_basicsky = 5

    ruleNames = ["root", "expr", "sky", "msky", "rsky", "basicsky"]

    EOF = Token.EOF
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

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext, 0)

        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRoot"):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)

    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.expr()
            self.state = 13
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sky(self):
            return self.getTypedRuleContext(SkylineParser.SkyContext, 0)

        def IDENT(self):
            return self.getToken(SkylineParser.IDENT, 0)

        def ASSIGN(self):
            return self.getToken(SkylineParser.ASSIGN, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpr"):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)

    def expr(self):

        localctx = SkylineParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 0, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.sky()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(SkylineParser.IDENT)
                self.state = 17
                self.match(SkylineParser.ASSIGN)
                self.state = 18
                self.sky()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SkyContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def msky(self, i: int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.MskyContext)
            else:
                return self.getTypedRuleContext(SkylineParser.MskyContext, i)

        def SUM(self, i: int=None):
            if i is None:
                return self.getTokens(SkylineParser.SUM)
            else:
                return self.getToken(SkylineParser.SUM, i)

        def RES(self, i: int=None):
            if i is None:
                return self.getTokens(SkylineParser.RES)
            else:
                return self.getToken(SkylineParser.RES, i)

        def NUM(self, i: int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_sky

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSky"):
                return visitor.visitSky(self)
            else:
                return visitor.visitChildren(self)

    def sky(self):

        localctx = SkylineParser.SkyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sky)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.msky()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == SkylineParser.RES or _la == SkylineParser.SUM:
                self.state = 28
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 1, self._ctx)
                if la_ == 1:
                    self.state = 22
                    self.match(SkylineParser.SUM)
                    self.state = 23
                    self.msky()
                    pass

                elif la_ == 2:
                    self.state = 24
                    self.match(SkylineParser.RES)
                    self.state = 25
                    self.match(SkylineParser.NUM)
                    pass

                elif la_ == 3:
                    self.state = 26
                    self.match(SkylineParser.SUM)
                    self.state = 27
                    self.match(SkylineParser.NUM)
                    pass

                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MskyContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rsky(self, i: int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.RskyContext)
            else:
                return self.getTypedRuleContext(SkylineParser.RskyContext, i)

        def MUL(self, i: int=None):
            if i is None:
                return self.getTokens(SkylineParser.MUL)
            else:
                return self.getToken(SkylineParser.MUL, i)

        def NUM(self, i: int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_msky

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMsky"):
                return visitor.visitMsky(self)
            else:
                return visitor.visitChildren(self)

    def msky(self):

        localctx = SkylineParser.MskyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_msky)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.rsky()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == SkylineParser.MUL:
                self.state = 38
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
                if la_ == 1:
                    self.state = 34
                    self.match(SkylineParser.MUL)
                    self.state = 35
                    self.rsky()
                    pass

                elif la_ == 2:
                    self.state = 36
                    self.match(SkylineParser.MUL)
                    self.state = 37
                    self.match(SkylineParser.NUM)
                    pass

                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RskyContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicsky(self):
            return self.getTypedRuleContext(SkylineParser.BasicskyContext, 0)

        def RES(self, i: int=None):
            if i is None:
                return self.getTokens(SkylineParser.RES)
            else:
                return self.getToken(SkylineParser.RES, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_rsky

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRsky"):
                return visitor.visitRsky(self)
            else:
                return visitor.visitChildren(self)

    def rsky(self):

        localctx = SkylineParser.RskyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rsky)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == SkylineParser.RES:
                self.state = 43
                self.match(SkylineParser.RES)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.basicsky()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BasicskyContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sky(self):
            return self.getTypedRuleContext(SkylineParser.SkyContext, 0)

        def EDIF(self):
            return self.getToken(SkylineParser.EDIF, 0)

        def EDIFS(self):
            return self.getToken(SkylineParser.EDIFS, 0)

        def RAND(self):
            return self.getToken(SkylineParser.RAND, 0)

        def IDENT(self):
            return self.getToken(SkylineParser.IDENT, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_basicsky

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBasicsky"):
                return visitor.visitBasicsky(self)
            else:
                return visitor.visitChildren(self)

    def basicsky(self):

        localctx = SkylineParser.BasicskyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_basicsky)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(SkylineParser.T__0)
                self.state = 52
                self.sky()
                self.state = 53
                self.match(SkylineParser.T__1)
                pass
            elif token in [SkylineParser.EDIF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(SkylineParser.EDIF)
                pass
            elif token in [SkylineParser.EDIFS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.match(SkylineParser.EDIFS)
                pass
            elif token in [SkylineParser.RAND]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(SkylineParser.RAND)
                pass
            elif token in [SkylineParser.IDENT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 58
                self.match(SkylineParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
