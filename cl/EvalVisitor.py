import sys
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor
sys.path.append('../')
from skyline import Skyline  # noqa: E402


# El visitor per avaluar una expressió de Skyline
class EvalVisitor(SkylineVisitor):

    # inicialitza la taula de símbols
    def __init__(self, taula):
        self.tsimb = taula

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx: SkylineParser.RootContext):
        ch = next(ctx.getChildren())
        return self.visit(ch)

    # Visit a parse tree produced by SkylineParser#expr.
    # retorna el Skyline resultant d'expressió i actualitza la taula de símbols si necessita
    def visitExpr(self, ctx: SkylineParser.ExprContext):
        chs = [n for n in ctx.getChildren()]
        if len(chs) == 3:
            iden = chs[0].getText()
            v = self.visit(chs[2])
            self.tsimb[iden] = v
            return v
        return self.visit(chs[0])

    # Visit a parse tree produced by SkylineParser#sky.
    # retorna el resultat d'unió i desplaçament
    def visitSky(self, ctx: SkylineParser.SkyContext):
        chs = [n for n in ctx.getChildren()]
        sky = self.visit(chs[0])
        i = 1
        while i < len(chs):
            if chs[i].getText() == '-':
                num = int(chs[i+1].getText())
                sky = sky.getDesp(-num)
            else:
                txt = chs[i+1].getText()
                if txt[0] >= '0' and txt[0] <= '9':
                    num = int(txt)
                    sky = sky.getDesp(num)
                else:
                    sky = sky.getUnio(self.visit(chs[i+1]))
            i += 2
        return sky

    # Visit a parse tree produced by SkylineParser#msky.
    # retorna el resultat d'intersecció i replicació
    def visitMsky(self, ctx: SkylineParser.MskyContext):
        chs = [n for n in ctx.getChildren()]
        sky = self.visit(chs[0])
        i = 2
        while i < len(chs):
            txt = chs[i].getText()
            if txt[0] >= '0' and txt[0] <= '9':
                num = int(txt)
                sky = sky.getRep(num)
            else:
                sky = sky.getInterseccio(self.visit(chs[i]))
            i += 2
        return sky

    # Visit a parse tree produced by SkylineParser#rsky.
    # retorna el resultat de reflectir un Skyline
    def visitRsky(self, ctx: SkylineParser.RskyContext):
        chs = [n for n in ctx.getChildren()]
        sky = self.visit(chs[len(chs)-1])
        if len(chs) % 2 == 0:
            sky = sky.getReflect()
        return sky

    # Visit a parse tree produced by SkylineParser#basicsky.
    # retorna un Skyline simple
    def visitBasicsky(self, ctx: SkylineParser.BasicskyContext):
        chs = [n for n in ctx.getChildren()]
        if len(chs) == 3:
            return self.visit(chs[1])
        txt = chs[0].getText()
        if txt[0] == '(':
            nums = [int(n) for n in txt[1:(len(txt)-1)].split(',')]
            return Skyline([(nums[0], nums[1], nums[2])])
        if txt[0] == '{':
            nums = [int(n) for n in txt[1:(len(txt)-1)].split(',')]
            return Skyline.aleatori(nums[0], nums[1], nums[2], nums[3], nums[4])
        if txt[0] == '[':
            nums = txt[1:len(txt)-1].split(',')
            i = 0
            edifs = []
            while i < len(nums):
                edifs.append((int(nums[i][1:]), int(nums[i+1]), int(nums[i+2][:(len(nums[i+2])-1)])))
                i += 3
            return Skyline(edifs)
        return self.tsimb[txt]


del SkylineParser
