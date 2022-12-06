class Les():
    def __init__(self):
        self.vetor = [None, None, None, None, None]
        self.quant = 0

    def getQuant(self):
        return self.quant
    
    def InserirFim(self, valor):
        self.vetor[self.quant] = valor
        self.quant+=1

    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=" ")
        print()

    def estaCheia(self):
        '''if self.quant == 5:
            return True
        else:
            return False'''
        return self.quant == 5

    def estaVazia(self):
        return self.quant == 0

    def RemoverFim(self):
        self.quant-=1

    def InserirInicio(self, valor):
        i = self.quant
        for i in range(self.quant, 0, -1):
            self.vetor[i] = self.vetor[i-1]
            i-=1
        self.vetor[0] = valor
        self.quant+=1

    def RemoverInicio(self):
        for i in range(self.quant-1):
            self.vetor[i] = self.vetor[i+1]
        self.quant-=1        

    def getPrim(self):
        return self.vetor[0]
    
    def getUlt(self):
        return self.vetor[self.quant-1]


    def InserirAposDet(self,valor1,valor2):
        for i in range(self.quant):
            if self.vetor[i] == valor2:
                pos = i+1
                j = self.quant
                while j != pos:
                    self.vetor[j]=self.vetor[j-1]
                    j-=1
        self.vetor[j] = valor1
        self.quant+=1
