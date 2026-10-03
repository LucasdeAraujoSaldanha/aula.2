# class Carro:
#     marca= "Honda" 
#     modelo="Civic"

#     def __init__(self, cor,ano):
#         self.cor = cor 
#         self.ano = ano 

#     def __str__(self):
#         return f'Marca: {self.marca} | Modelo: {self.modelo}'

#     def acelerar(self):
#         print('Acelerando.........................')

#     def ligar(self):
#         print('ligando')

        

# carro1 = Carro('branco', 2022)

# print(carro1.cor)
# print(carro1.ano)

# print(carro1.modelo)


# carro2 = Carro('vermelo', 2027)

# carro2.modelo = 'Citi'

# print(carro1.cor)
# print(carro1.ano)

# carro2.ligar()

class personagem:
    vida = 100
    moedas = 0
    nivel = 1
    statos = 'pobres'

    def __init__(self, nome, clase, familia):
        self.nome = nome 
        self.clase = clase
        self.familia = familia 

    def dano(self, valor):
        self.vida -= valor
        if (self.vida <= 0):
            print('Você tomou {self.valor} de dano e morreu!\nFaz o L')
        else:
            print(F'Você tomou {self.valor} de dano')
            
    def dinheiro(self, valor):
        dinheiro_enprestado = int(input('Você encontra um agiota, ele oferece um inprestimo, quanto deseja?'))
        self.dinheiro += valor 
        print(F'Você pegou {self.dinheiro} imprestado')

Personagem = personagem('Jorginho', 'Mago', 'Aewubof' )

Personagem.dinheiro()

