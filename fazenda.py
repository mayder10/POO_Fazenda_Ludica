# --- Classe Base: Animal ---
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "O animal emite um som."

    def apresentar(self):
        return f"Olá, sou {self.nome} e tenho {self.idade} anos."


# --- Subclasse: Cachorro ---
class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        return "Au! Au!"


# --- Subclasse: Gato ---
class Gato(Animal):
    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        return "Miau!"


# --- Subclasse: Vaca (com Encapsulamento) ---
class Vaca(Animal):
    def __init__(self, nome, idade, producao_leite_litros):
        super().__init__(nome, idade)
        self.__producao_leite_litros = producao_leite_litros  # atributo privado

    def emitir_som(self):
        return "Muuu!"

    # Getter
    def obter_producao_leite(self):
        return self.__producao_leite_litros

    # Setter
    def registrar_ordenha(self, litros):
        self.__producao_leite_litros = litros


# --- Testes/Demonstração ---
c1 = Cachorro("Rex", 3, "Labrador")
g1 = Gato("Mimi", 5, "Branco")
v1 = Vaca("Mimosa", 7, 25.5)

print(c1.apresentar(), "-", c1.emitir_som())
print(g1.apresentar(), "-", g1.emitir_som())
print(v1.apresentar(), "-", v1.emitir_som())

# Testando encapsulamento
print("\nProdução de leite atual:", v1.obter_producao_leite(), "litros")

v1.registrar_ordenha(28.0)
print("Produção de leite após ordenha:", v1.obter_producao_leite(), "litros")
