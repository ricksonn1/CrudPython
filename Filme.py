class Filme:

    def __init__(self, id, nome, ano, duracao):
        self.id = id
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

    def setNome(self, nome):
        self.nome = nome

    def setAno(self, ano):
        self.ano = ano

    def setDuracao(self, duracao):
        self.duracao

    def getNome(self):
        return self.nome

    def getAno(self):
        return self.ano

    def getDuracao(self):
        return self.duracao

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id