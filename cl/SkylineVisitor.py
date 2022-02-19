# Generated from Skyline.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser


# This class defines a complete generic visitor for a parse tree produced by SkylineParser.
class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx: SkylineParser.RootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx: SkylineParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#sky.
    def visitSky(self, ctx: SkylineParser.SkyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#msky.
    def visitMsky(self, ctx: SkylineParser.MskyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#rsky.
    def visitRsky(self, ctx: SkylineParser.RskyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#basicsky.
    def visitBasicsky(self, ctx: SkylineParser.BasicskyContext):
        return self.visitChildren(ctx)

del SkylineParser
