from random import randint


# classe Skyline: guarda area, alcada i una llista ordenada d'edificis disjunts
# els edificis son en forma de tuples (xmin, alc, xmax)
class Skyline:

    # construir skyline a partir d'una llista d'edificis
    def __init__(self, llista):
        self.area = 0
        self.alcada = 0
        n = len(llista)
        if n == 0:
            self.edif = []
        elif n == 1:
            self.edif = llista
            self.area = (llista[0][2] - llista[0][0])*llista[0][1]
            self.alcada = llista[0][1]
            if self.alcada <= 0 or llista[0][2] <= llista[0][0]:
                self.edif = []
                self.area = 0
                self.alcada = 0
        else:
            tmp1 = Skyline(llista[:n//2])
            tmp2 = Skyline(llista[n//2:])
            tmp3 = tmp1.getUnio(tmp2)
            self.area = tmp3.area
            self.alcada = tmp3.alcada
            self.edif = tmp3.edif

    # construir aleatori
    @staticmethod
    def aleatori(n, h, w, xmin, xmax):
        llista = []
        if xmax > xmin:
            for i in range(0, n):
                alcada = randint(0, h)
                if alcada != 0:
                    posmin = randint(xmin, xmax-1)
                    posmax = posmin + randint(1, min(w, xmax-posmin))
                    llista.append((posmin, alcada, posmax))
        return Skyline(llista)

    # obtenir area
    def getArea(self):
        return self.area

    # obtenir alcada
    def getAlcada(self):
        return self.alcada

    # obtenir edificis
    def getEdif(self):
        return self.edif

    # obtenir reflectit
    def getReflect(self):
        sky = Skyline([])
        sky.area = self.area
        sky.alcada = self.alcada
        edif1 = self.edif
        edif2 = []
        n = len(edif1)
        if n > 0:
            ini = edif1[0][0]
            for i in range(1, n):
                ampl = edif1[n-i][2] - edif1[n-i][0]
                edif2.append((ini, edif1[n-i][1], ini+ampl))
                ini = ini + ampl + (edif1[n-i][0] - edif1[n-i-1][2])
            ampl = edif1[0][2] - edif1[0][0]
            edif2.append((ini, edif1[0][1], ini+ampl))
        sky.edif = edif2
        return sky

    # desplacament
    def getDesp(self, n):
        sky = Skyline([])
        sky.area = self.area
        sky.alcada = self.alcada
        edif1 = self.edif
        edif2 = []
        for xmin, alc, xmax in edif1:
            edif2.append((xmin+n, alc, xmax+n))
        sky.edif = edif2
        return sky

    # replicacio
    def getRep(self, n):
        sky = Skyline([])
        sky.area = self.area*n
        sky.alcada = self.alcada
        edif1 = self.edif
        edif2 = []
        m = 0
        suma = edif1[(len(edif1)-1)][2] - edif1[0][0]
        for i in range(0, n):
            for xmin, alc, xmax in edif1:
                edif2.append((xmin+m, alc, xmax+m))
            m += suma
        sky.edif = edif2
        return sky

    # retorna interseccio de dos edificis
    @staticmethod
    def interseccio2(ed1, ed2):
        h1 = ed1[1]
        h2 = ed2[1]
        if ed1[2] <= ed2[0] or ed1[0] >= ed2[2]:
            return []
        if ed1[2] >= ed2[2] and ed1[0] <= ed2[0]:
            return [(ed2[0], min(h1, h2), ed2[2])]
        if ed2[2] >= ed1[2] and ed2[0] <= ed1[0]:
            return [(ed1[0], min(h1, h2), ed1[2])]
        if ed1[2] > ed2[0] and ed1[0] < ed2[0]:
            return [(ed2[0], min(h1, h2), ed1[2])]
        return [(ed1[0], min(h1, h2), ed2[2])]

    # append al final de edif o fa merge amb l'ultim element
    def appended(self, ed):
        if ed[1] > self.alcada:
            self.alcada = ed[1]
        self.area += (ed[2] - ed[0])*ed[1]
        if len(self.edif) != 0:
            last = self.edif[len(self.edif)-1]
            if last[1] == ed[1] and last[2] == ed[0]:
                self.edif[len(self.edif)-1] = (last[0], last[1], ed[2])
            else:
                self.edif.append(ed)
        else:
            self.edif.append(ed)

    # interseccio amb un altre skyline
    def getInterseccio(self, sky2):
        sky = Skyline([])
        n1 = 0
        n2 = 0
        while n1 < len(self.edif) and n2 < len(sky2.edif):
            if self.edif[n1][2] <= sky2.edif[n2][0]:
                n1 += 1
            elif sky2.edif[n2][2] <= self.edif[n1][0]:
                n2 += 1
            else:
                intersec = Skyline.interseccio2(self.edif[n1], sky2.edif[n2])
                sky.appended(intersec[0])
                if self.edif[n1][2] <= sky2.edif[n2][2]:
                    n1 += 1
                else:
                    n2 += 1
        return sky

    # retorna unio de dos edificis amb mateix xmax
    @staticmethod
    def unio2(ed1, ed2):
        if ed1[0] == ed2[0]:
            return [(ed1[0], max(ed1[1], ed2[1]), ed1[2])]
        if ed1[0] < ed2[0]:
            return[(ed1[0], ed1[1], ed2[0]), (ed2[0], max(ed1[1], ed2[1]), ed2[2])]
        return[(ed2[0], ed2[1], ed1[0]), (ed1[0], max(ed1[1], ed2[1]), ed1[2])]

    # unio amb un altre skyline
    def getUnio(self, sky2):
        sky = Skyline([])
        n1 = 0
        n2 = 0
        current = 0
        value = (0, 0, 0)
        while n1 < len(self.edif) and n2 < len(sky2.edif):
            ed1 = self.edif[n1]
            ed2 = sky2.edif[n2]
            if ed1[2] <= ed2[0]:
                sky.appended(ed1)
                if current == 1:
                    self.edif[n1] = value
                    current = 0
                n1 += 1
            elif ed2[2] <= ed1[0]:
                sky.appended(ed2)
                if current == 2:
                    sky2.edif[n2] = value
                    current = 0
                n2 += 1
            elif ed1[2] == ed2[2]:
                un = Skyline.unio2(ed1, ed2)
                for ed in un:
                    sky.appended(ed)
                if current == 1:
                    self.edif[n1] = value
                    current = 0
                n1 += 1
                if current == 2:
                    sky2.edif[n2] = value
                    current = 0
                n2 += 1
            elif ed1[2] < ed2[2]:
                if current != 2:
                    if current == 1:
                        self.edif[n1] = value
                    current = 2
                    value = ed2
                sky2.edif[n2] = (ed1[2], ed2[1], ed2[2])
                ed2 = (ed2[0], ed2[1], ed1[2])
                un = Skyline.unio2(ed1, ed2)
                for ed in un:
                    sky.appended(ed)
                n1 += 1
            else:
                if current != 1:
                    if current == 2:
                        sky2.edif[n2] = value
                    current = 1
                    value = ed1
                self.edif[n1] = (ed2[2], ed1[1], ed1[2])
                ed1 = (ed1[0], ed1[1], ed2[2])
                un = Skyline.unio2(ed1, ed2)
                for ed in un:
                    sky.appended(ed)
                n2 += 1
        if n1 < len(self.edif):
            sky.appended(self.edif[n1])
            if current == 1:
                self.edif[n1] = value
                current = 0
            n1 += 1
            while n1 < len(self.edif):
                sky.appended(self.edif[n1])
                if current == 1:
                    self.edif[n1] = value
                    current = 0
                n1 += 1
        if n2 < len(sky2.edif):
            sky.appended(sky2.edif[n2])
            if current == 2:
                sky2.edif[n2] = value
                current = 0
            n2 += 1
            while n2 < len(sky2.edif):
                sky.appended(sky2.edif[n2])
                if current == 2:
                    sky2.edif[n2] = value
                    current = 0
                n2 += 1
        return sky
