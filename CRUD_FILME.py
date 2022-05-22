from Filme import Filme


class Filmes:
    listFilm = []

    def cadastrarFilme(self):
        id = int(input("Digite o id do filme: \n"))
        nome = (input("Digite o nome do filme: \n"))
        ano = (input("Digite o ano do filme: \n"))
        duracao = (input("Digite a duração do filme: \n"))


        filme = Filme(id, nome, ano, duracao)

        self.listFilm.append(filme)

    def listarFilme(self):
        for filme in (self.listFilm):
            print("=====================")
            print(filme.getId())
            print(filme.getNome())
            print(filme.getAno())
            print(filme.getDuracao())
            print("=====================")

    def deletarFilme(self):
        id = int(input("Digite o id do filme para deletar: \n"))
        for film in self.listFilm:
            if film.getId() == id:
                self.listFilm.remove(film)
                print("Filme deletado com sucesso!")

    def alterarFilme(self):
        id = int(input("Digite o id do filme para alterar: \n"))
        nome = (input("Digite o novo nome do filme: \n"))
        ano = (input("Digite o novo ano do filme: \n"))
        duracao = (input("Digite a nova duração do filme: \n"))

        for i in range(len(self.listFilm)):
            if self.listFilm[i].getId() == id:
                filme = Filme(id, nome, ano, duracao)
                self.listFilm[i] = filme

    def buscarFilmes(self):
        idFilme = int(input("Qual id do filme? \n"))
        for film in self.listFilm:
            if film.getId() == idFilme:
                print("=====================")
                print(film.getId())
                print(film.getNome())
                print(film.getAno())
                print(film.getDuracao)
                print("=====================")
                break

    def menu(self):
        while True:
            print(
                " \n 1: Cadastrar filmes.\n 2: Listar filmes.\n 3: Deletar filmes.\n 4: Alterar dados do filme.\n 5: Buscar filme.")
            opcao = input("Digite a opção desejada: \n")
            if opcao == "1":
                self.cadastrarFilme()
            elif opcao == "2":
                self.listarFilme()
            elif opcao == "3":
                self.deletarFilme()
            elif opcao == "4":
                self.alterarFilme()
            elif opcao == "5":
                self.buscarFilmes()
            else:
                print("Filme não está cadastrado!")


if __name__ == "__main__":
    filmes = Filmes()
    filmes.menu()
