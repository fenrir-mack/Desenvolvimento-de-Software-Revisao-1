class Carro:
    def __init__(self, cor, modelo, marca, quilometragem,ano,potencia):
        self.cor = cor
        self.modelo = modelo
        self.marca = marca
        self.__quilometragem = quilometragem
        self._ano = ano
        self.potencia = potencia

    def __str__(self):
        return (f"{self.marca} {self.modelo} ({self._ano})\n"
                f"Cor: {self.cor}\n"
                f"Quilometragem: {self.__quilometragem} km\n"
                f"Potência: {self.potencia} cv")


p1 = Carro("Vermelho","HB20","Chevrolet",10000,2020,100)


print(p1)
